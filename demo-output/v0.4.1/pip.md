# coldstep detect digest — `pip`

> **Faithful summary of real coldstep telemetry.** Extracted from the unmodified `.coldstep-events.jsonl` produced by [this run](https://github.com/coldstep-io/coldstep-demo/actions/runs/27513829354) (coldstep agent `v0.4.0`, action `@v0.4.1`, `mode: detect`, profile `enhanced`). At v0.4.1 coldstep posts the rendered digest only to the GitHub **Step Summary**; this file summarizes the same events so you can read them here. v0.5.x writes a committable digest file directly — see `../v0.5.3/`.

**Install command:** `pip install pandas numpy scikit-learn matplotlib`  
**Kernel:** `6.17.0-1018-azure`  
**Run:** [27513829354](https://github.com/coldstep-io/coldstep-demo/actions/runs/27513829354) · job `pip-demo` · sha `58dcafb`

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

71 fork events; 15 `exec()` calls captured. Binaries executed:

- `node` → `/home/runner/actions-runner/cached/2.335.1/externals/node24/bin/node`
- `bash` → `/usr/bin/bash`
- `pip` → `/usr/bin/pip`
- `lsb_release` → `/usr/bin/lsb_release`
- `getopt` → `/usr/bin/getopt`
- `cut` → `/usr/bin/cut`
- `tr` → `/usr/bin/tr`
- `uname` → `/usr/bin/uname`
- `rustc` → `/home/runner/.cargo/bin/rustc`
- `rustc` → `/home/runner/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/bin/rustc`
- `node` → `/home/runner/actions-runner/cached/2.335.1/externals/node20/bin/node`

## IPv4 egress

Every distinct IPv4 destination the install touched (TCP connects + UDP datagrams):

| destination | port(s) | by | policy | events |
| :---------- | :------ | :- | :----- | -----: |
| `168.63.129.16` | 53,80,32526 | python3, systemd-resolve | monitor | 38 |
| `127.0.0.53` | 53 | node, pip, provjobd2072795 | monitor | 11 |
| `127.0.0.1` | 32789,33548,33748,45340,48080 | systemd-resolve | monitor | 8 |
| `151.101.128.223` | 443 | pip | monitor | 4 |
| `151.101.192.223` | 443 | pip | monitor | 2 |
| `151.101.64.223` | 443 | pip | monitor | 2 |
| `151.101.0.223` | 443 | pip | monitor | 2 |
| `20.75.202.224` | 443 | provjobd2072795 | monitor | 1 |
| `140.82.113.22` | 443 | node | monitor | 1 |

IPv6 destinations seen (not enforced in this profile): `2a04:4e42:200::223`, `2a04:4e42:400::223`, `2a04:4e42:600::223`, `2a04:4e42::223`

## TLS SNI (logical hosts inside TLS)

| SNI host | resolved dst IP(s) | by | events |
| :------- | :----------------- | :- | -----: |
| `pypi.org` | `151.101.128.223` | pip | 1 |
| `files.pythonhosted.org` | `151.101.128.223` | pip | 1 |
| `hosted-compute-watchdog-prod-eus-02.githubapp.com` | `20.75.202.224` | provjobd2072795 | 1 |
| `results-receiver.actions.githubusercontent.com` | `140.82.113.22` | node | 1 |

## HTTP host headers (cleartext)

| host | sample path | by |
| :--- | :---------- | :- |
| `168.63.129.16` | `/machine/?comp=goalstate` | python3 |

## Filesystem activity

create: 5000

---
_Raw telemetry: `.coldstep-events.jsonl` (5,258 events) is attached to the [run artifacts](https://github.com/coldstep-io/coldstep-demo/actions/runs/27513829354)._
