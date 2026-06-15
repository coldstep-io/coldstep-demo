# coldstep detect digest — `pip`

> **Faithful summary of real coldstep telemetry.** Extracted from the unmodified `.coldstep-events.jsonl` produced by [this run](https://github.com/coldstep-io/coldstep-demo/actions/runs/27519463249) (coldstep agent `v0.5.3`, action `@v0.5.3`, `mode: detect`, profile `enhanced`). coldstep posts the rendered digest to the GitHub **Step Summary**; this file summarizes the same events so you can read them here without opening Actions. The raw telemetry is the source of truth — linked at the bottom.

**Install command:** `pip install pandas numpy scikit-learn matplotlib`  
**Kernel:** `6.17.0-1018-azure`  
**Run:** [27519463249](https://github.com/coldstep-io/coldstep-demo/actions/runs/27519463249) · job `pip-demo` · sha `a7ecac0`

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

101 fork events; 23 `exec()` calls captured. Binaries executed:

- `node` → `/home/runner/actions-runner/cached/2.335.1/externals/node24/bin/node`
- `networkctl` → `/usr/bin/networkctl`
- `net-interface-h` → `/usr/lib/open-iscsi/net-interface-handler`
- `chrony-onofflin` → `/usr/lib/networkd-dispatcher/off.d/chrony-onoffline`
- `systemd-sysctl` → `/usr/lib/systemd/systemd-sysctl`
- `chronyc` → `/usr/bin/chronyc`
- `bash` → `/usr/bin/bash`
- `pip` → `/usr/bin/pip`
- `lsb_release` → `/usr/bin/lsb_release`
- `getopt` → `/usr/bin/getopt`
- `cut` → `/usr/bin/cut`
- `tr` → `/usr/bin/tr`
- `uname` → `/usr/bin/uname`
- `rustc` → `/home/runner/.cargo/bin/rustc`
- `rustc` → `/home/runner/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/bin/rustc`
- `9` → `/proc/self/fd/9`
- `e2scrub_all` → `/sbin/e2scrub_all`
- `node` → `/home/runner/actions-runner/cached/2.335.1/externals/node20/bin/node`

## IPv4 egress

Every distinct IPv4 destination the install touched (TCP connects + UDP datagrams):

| destination | port(s) | by | policy | events |
| :---------- | :------ | :- | :----- | -----: |
| `168.63.129.16` | 53,80,32526 | python3, systemd-resolve | monitor | 48 |
| `127.0.0.53` | 53 | hosted-compute-, node, pip | monitor | 11 |
| `127.0.0.1` | 36007,39540,45714,50695,56098 | systemd-resolve | monitor | 8 |
| `151.101.0.223` | 443 | pip | monitor | 4 |
| `151.101.192.223` | 443 | pip | monitor | 2 |
| `151.101.128.223` | 443 | pip | monitor | 2 |
| `151.101.64.223` | 443 | pip | monitor | 2 |
| `140.82.113.23` | 443 | hosted-compute- | monitor | 1 |
| `140.82.113.22` | 443 | node | monitor | 1 |

IPv6 destinations seen (not enforced in this profile): `2a04:4e42:200::223`, `2a04:4e42:400::223`, `2a04:4e42:600::223`, `2a04:4e42::223`

## TLS SNI (logical hosts inside TLS)

| SNI host | resolved dst IP(s) | by | events |
| :------- | :----------------- | :- | -----: |
| `hosted-compute-request-orchestrator-prod-iad-01.githubapp.com` | `140.82.113.23` | hosted-compute- | 1 |
| `pypi.org` | `151.101.0.223` | pip | 1 |
| `files.pythonhosted.org` | `151.101.0.223` | pip | 1 |
| `results-receiver.actions.githubusercontent.com` | `140.82.113.22` | node | 1 |

## HTTP host headers (cleartext)

| host | sample path | by |
| :--- | :---------- | :- |
| `168.63.129.16` | `/machine/?comp=goalstate` | python3 |

## Filesystem activity

create: 5000

---
_Raw telemetry: `.coldstep-events.jsonl` (5,317 events) is attached to the [run artifacts](https://github.com/coldstep-io/coldstep-demo/actions/runs/27519463249)._
