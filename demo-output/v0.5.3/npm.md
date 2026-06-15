# coldstep detect digest — `npm`

> **Faithful summary of real coldstep telemetry.** Extracted from the unmodified `.coldstep-events.jsonl` produced by [this run](https://github.com/coldstep-io/coldstep-demo/actions/runs/27519462576) (coldstep agent `v0.5.3`, action `@v0.5.3`, `mode: detect`, profile `enhanced`). coldstep posts the rendered digest to the GitHub **Step Summary**; this file summarizes the same events so you can read them here without opening Actions. The raw telemetry is the source of truth — linked at the bottom.

**Install command:** `npm install express && npm install @aws-sdk/client-s3`  
**Kernel:** `6.17.0-1018-azure`  
**Run:** [27519462576](https://github.com/coldstep-io/coldstep-demo/actions/runs/27519462576) · job `npm-demo` · sha `a7ecac0`

## BPF program health

11/12 probes loaded — the digest is not blind.

| probe | loaded |
| :---- | :----- |
| `sched_process_exec` | ✅ |
| `raw_tp/sys_enter (connect, sendto, http sniff, tls)` | ✅ |
| `dns recvfrom sniff` | ✅ |
| `btf` | ✅ |
| `kprobe tcp_v4_connect (connect_result)` | ✅ |
| `tp/sock/inet_sock_set_state` | ✅ |
| `raw_tp/io_uring_submit_sqe` | ❌ (no such file or directory) |
| `sched_process_fork` | ✅ |
| `raw_tp/sys_enter (fs)` | ✅ |
| `raw_tp/sys_enter (ktls)` | ✅ |
| `cgroup/connect6+sendmsg6 (ipv6_obs)` | ✅ |
| `raw_tp/sys_enter (bpf audit)` | ✅ |

## Processes

59 fork events; 10 `exec()` calls captured. Binaries executed:

- `node` → `/home/runner/actions-runner/cached/2.335.1/externals/node24/bin/node`
- `sh` → `/bin/sh`
- `debian-sa1` → `/usr/lib/sysstat/debian-sa1`
- `bash` → `/usr/bin/bash`
- `npm` → `/usr/local/bin/npm`
- `node` → `/usr/local/bin/node`
- `node` → `/home/runner/actions-runner/cached/2.335.1/externals/node20/bin/node`

## IPv4 egress

Every distinct IPv4 destination the install touched (TCP connects + UDP datagrams):

| destination | port(s) | by | policy | events |
| :---------- | :------ | :- | :----- | -----: |
| `168.63.129.16` | 53,80,32526 | python3, systemd-resolve | monitor | 27 |
| `104.16.1.34` | 0,443 | libuv-worker, npm install exp | monitor | 17 |
| `104.16.2.34` | 0,443 | libuv-worker, npm install @aw | monitor | 17 |
| `127.0.0.53` | 53 | .NET TP Worker, hosted-compute-, libuv-worker, node | monitor | 14 |
| `127.0.0.1` | 33573,34726,38224,50473,55999,57284 | systemd-resolve | monitor | 10 |
| `104.16.0.34` | 0 | libuv-worker | monitor | 2 |
| `104.16.5.34` | 0 | libuv-worker | monitor | 2 |
| `104.16.9.34` | 0 | libuv-worker | monitor | 2 |
| `104.16.11.34` | 0 | libuv-worker | monitor | 2 |
| `104.16.6.34` | 0 | libuv-worker | monitor | 2 |
| `104.16.4.34` | 0 | libuv-worker | monitor | 2 |
| `104.16.8.34` | 0 | libuv-worker | monitor | 2 |
| `104.16.7.34` | 0 | libuv-worker | monitor | 2 |
| `104.16.10.34` | 0 | libuv-worker | monitor | 2 |
| `104.16.3.34` | 0 | libuv-worker | monitor | 2 |
| `140.82.114.23` | 443 | hosted-compute- | monitor | 1 |
| `140.82.114.21` | 443 | node | monitor | 1 |

IPv6 destinations seen (not enforced in this profile): `2606:4700::6810:122`, `2606:4700::6810:22`, `2606:4700::6810:222`, `2606:4700::6810:322`, `2606:4700::6810:422`, `2606:4700::6810:522`, `2606:4700::6810:622`, `2606:4700::6810:722`, `2606:4700::6810:822`, `2606:4700::6810:922`, `2606:4700::6810:a22`, `2606:4700::6810:b22`

## TLS SNI (logical hosts inside TLS)

| SNI host | resolved dst IP(s) | by | events |
| :------- | :----------------- | :- | -----: |
| `registry.npmjs.org` | `104.16.1.34`, `104.16.2.34` | npm install @aw, npm install exp | 30 |
| `results-receiver.actions.githubusercontent.com` | `140.82.114.21` | .NET TP Worker, node | 2 |
| `hosted-compute-request-orchestrator-prod-iad-02.githubapp.com` | `140.82.114.23` | hosted-compute- | 1 |

## HTTP host headers (cleartext)

| host | sample path | by |
| :--- | :---------- | :- |
| `168.63.129.16` | `/machine/?comp=goalstate` | python3 |

## Filesystem activity

create: 5000

---
_Raw telemetry: `.coldstep-events.jsonl` (5,356 events) is attached to the [run artifacts](https://github.com/coldstep-io/coldstep-demo/actions/runs/27519462576)._
