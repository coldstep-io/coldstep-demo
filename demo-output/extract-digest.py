#!/usr/bin/env python3
"""Render a faithful coldstep detect digest from a committed .coldstep-events.jsonl.

The input is the raw, unmodified telemetry coldstep's eBPF agent writes during a
run. This script summarizes the same events coldstep renders into the GitHub
Step Summary, so the committed .md is a stand-in readers can browse without
opening Actions. It is intentionally a *summary*, not a byte-for-byte copy of
coldstep's own renderer.
"""
import sys, json, collections

path, pm, run_url, install_desc, action_tag, out_path = (
    sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5], sys.argv[6])

meta = None
execs = []
ip_by_dst = collections.defaultdict(lambda: {"ports": set(), "comms": set(), "policy": set(), "count": 0})
sni = collections.defaultdict(lambda: {"dst": set(), "comms": set(), "policy": set(), "count": 0})
http_hosts = collections.defaultdict(lambda: {"paths": set(), "comms": set(), "count": 0})
tcp6 = set()
fs_ops = collections.Counter()
proc_forks = 0
total = 0

with open(path, encoding="utf-8") as fh:
    for line in fh:
        line = line.strip()
        if not line:
            continue
        total += 1
        try:
            o = json.loads(line)
        except Exception:
            continue
        t = o.get("type")
        if t == "meta":
            meta = o
        elif t == "exec":
            execs.append((o.get("comm", "?"), o.get("exe", "?")))
        elif t in ("tcp", "udp"):
            d = o.get("dst")
            if d:
                e = ip_by_dst[d]
                e["ports"].add(o.get("dport"))
                e["comms"].add(o.get("comm", "?"))
                e["policy"].add(o.get("policy", "?"))
                e["count"] += 1
        elif t == "tcp6":
            d = o.get("dst")
            if d and ":" in d:  # only genuine IPv6 literals
                tcp6.add(d)
        elif t == "tls":
            s = o.get("sni")
            if s:
                e = sni[s]
                if o.get("dst"):
                    e["dst"].add(o["dst"])
                e["comms"].add(o.get("comm", "?"))
                e["policy"].add(o.get("policy", "?"))
                e["count"] += 1
        elif t == "http":
            h = o.get("host")
            if h:
                e = http_hosts[h]
                if o.get("path"):
                    e["paths"].add(o["path"])
                e["comms"].add(o.get("comm", "?"))
                e["count"] += 1
        elif t == "fs_event":
            fs_ops[o.get("op", "?")] += 1
        elif t == "proc_fork":
            proc_forks += 1

g = (meta or {}).get("github", {})
out = []
def w(s=""):
    out.append(s)

w(f"# coldstep detect digest — `{pm}`")
w()
w(f"> **Faithful summary of real coldstep telemetry.** Extracted from the unmodified "
  f"`.coldstep-events.jsonl` produced by [this run]({run_url}) "
  f"(coldstep agent `{(meta or {}).get('agent_version','?')}`, action `{action_tag}`, "
  f"`mode: detect`, profile `{(meta or {}).get('detect_profile','?')}`). "
  f"coldstep posts the rendered digest to the GitHub **Step Summary**; this file "
  f"summarizes the same events so you can read them here without opening Actions. "
  f"The raw telemetry is the source of truth — linked at the bottom.")
w()
w(f"**Install command:** `{install_desc}`  ")
w(f"**Kernel:** `{(meta or {}).get('kernel_release','?')}`  ")
w(f"**Run:** [{g.get('run_id','?')}]({run_url}) · job `{g.get('job','?')}` · sha `{(g.get('sha') or '')[:7]}`")
w()

w("## BPF program health")
w()
bpf = (meta or {}).get("bpf", [])
ok = sum(1 for b in bpf if b.get("ok"))
w(f"{ok}/{len(bpf)} probes loaded — the digest is not blind.")
w()
w("| probe | loaded |")
w("| :---- | :----- |")
for b in bpf:
    mark = "✅" if b.get("ok") else f"❌ ({b.get('detail','')})"
    w(f"| `{b.get('name','?')}` | {mark} |")
w()

w("## Processes")
w()
w(f"{proc_forks} fork events; {len(execs)} `exec()` calls captured. Binaries executed:")
w()
seen = set()
for comm, exe in execs:
    key = (comm, exe)
    if key in seen:
        continue
    seen.add(key)
    w(f"- `{comm}` → `{exe}`")
w()

w("## IPv4 egress")
w()
if ip_by_dst:
    w("Every distinct IPv4 destination the install touched (TCP connects + UDP datagrams):")
    w()
    w("| destination | port(s) | by | policy | events |")
    w("| :---------- | :------ | :- | :----- | -----: |")
    for dst, e in sorted(ip_by_dst.items(), key=lambda kv: -kv[1]["count"]):
        ports = ",".join(str(p) for p in sorted(x for x in e["ports"] if x is not None))
        comms = ", ".join(sorted(e["comms"]))
        pol = ",".join(sorted(e["policy"]))
        w(f"| `{dst}` | {ports} | {comms} | {pol} | {e['count']} |")
    w()
else:
    w("_No IPv4 egress recorded._")
    w()
if tcp6:
    w("IPv6 destinations seen (not enforced in this profile): " + ", ".join(f"`{a}`" for a in sorted(tcp6)))
    w()

w("## TLS SNI (logical hosts inside TLS)")
w()
if sni:
    w("| SNI host | resolved dst IP(s) | by | events |")
    w("| :------- | :----------------- | :- | -----: |")
    for host, e in sorted(sni.items(), key=lambda kv: -kv[1]["count"]):
        dsts = ", ".join(f"`{d}`" for d in sorted(e["dst"]))
        comms = ", ".join(sorted(e["comms"]))
        w(f"| `{host}` | {dsts} | {comms} | {e['count']} |")
    w()
else:
    w("_No TLS SNI captured._")
    w()

if http_hosts:
    w("## HTTP host headers (cleartext)")
    w()
    w("| host | sample path | by |")
    w("| :--- | :---------- | :- |")
    for host, e in sorted(http_hosts.items(), key=lambda kv: -kv[1]["count"]):
        path_s = sorted(e["paths"])[0] if e["paths"] else ""
        comms = ", ".join(sorted(e["comms"]))
        w(f"| `{host}` | `{path_s}` | {comms} |")
    w()

w("## Filesystem activity")
w()
w(", ".join(f"{op}: {n}" for op, n in fs_ops.most_common()) or "_none_")
w()
w("---")
w(f"_Raw telemetry: `.coldstep-events.jsonl` ({total:,} events) is attached to "
  f"the [run artifacts]({run_url})._")

with open(out_path, "w", encoding="utf-8") as fo:
    fo.write("\n".join(out) + "\n")
print(f"wrote {out_path} ({len(chr(10).join(out))} bytes)")
