# coldstep detect digest — `gem`

> **Faithful summary of real coldstep telemetry.** Extracted from the unmodified `.coldstep-events.jsonl` produced by [this run](https://github.com/coldstep-io/coldstep-demo/actions/runs/27519466042) (coldstep agent `v0.5.3`, action `@v0.5.3`, `mode: detect`, profile `enhanced`). coldstep posts the rendered digest to the GitHub **Step Summary**; this file summarizes the same events so you can read them here without opening Actions. The raw telemetry is the source of truth — linked at the bottom.

**Install command:** `gem install jekyll`  
**Kernel:** `6.17.0-1018-azure`  
**Run:** [27519466042](https://github.com/coldstep-io/coldstep-demo/actions/runs/27519466042) · job `gem-demo` · sha `a7ecac0`

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

337 fork events; 272 `exec()` calls captured. Binaries executed:

- `node` → `/home/runner/actions-runner/cached/2.335.1/externals/node24/bin/node`
- `bash` → `/usr/bin/bash`
- `sudo` → `/usr/bin/sudo`
- `gem` → `/usr/bin/gem`
- `ruby` → `/usr/bin/ruby`
- `networkctl` → `/usr/bin/networkctl`
- `net-interface-h` → `/usr/lib/open-iscsi/net-interface-handler`
- `chrony-onofflin` → `/usr/lib/networkd-dispatcher/off.d/chrony-onoffline`
- `chronyc` → `/usr/bin/chronyc`
- `systemd-sysctl` → `/usr/lib/systemd/systemd-sysctl`
- `ruby3.2` → `/usr/bin/ruby3.2`
- `make` → `/usr/bin/make`
- `rm` → `/usr/bin/rm`
- `sh` → `/bin/sh`
- `echo` → `/usr/bin/echo`
- `x86_64-linux-gn` → `/usr/bin/x86_64-linux-gnu-gcc`
- `cc1` → `/usr/libexec/gcc/x86_64-linux-gnu/13/cc1`
- `as` → `/usr/bin/as`
- `collect2` → `/usr/libexec/gcc/x86_64-linux-gnu/13/collect2`
- `ld` → `/usr/bin/ld`
- `mkdir` → `/bin/mkdir`
- `install` → `/usr/bin/install`
- `x86_64-linux-gn` → `/usr/bin/x86_64-linux-gnu-pkg-config`
- `x86_64-linux-gn` → `/usr/bin/x86_64-linux-gnu-g++`
- `cc1plus` → `/usr/libexec/gcc/x86_64-linux-gnu/13/cc1plus`
- `node` → `/home/runner/actions-runner/cached/2.335.1/externals/node20/bin/node`

## IPv4 egress

Every distinct IPv4 destination the install touched (TCP connects + UDP datagrams):

| destination | port(s) | by | policy | events |
| :---------- | :------ | :- | :----- | -----: |
| `168.63.129.16` | 53,80,32526 | python3, systemd-resolve | monitor | 85 |
| `127.0.0.53` | 53 | .NET TP Worker, hosted-compute-, node, provjobd2567565, ruby | monitor | 13 |
| `127.0.0.1` | 39165,46011,48226,48858,50896,52126,55544 | systemd-resolve | monitor | 10 |
| `20.75.202.224` | 443 | hosted-compute-, provjobd2567565 | monitor | 2 |
| `151.101.65.227` | 443 | ruby | monitor | 2 |
| `169.254.169.254` | 80 | python3 | monitor | 2 |
| `151.101.129.227` | 443 | ruby | monitor | 1 |
| `151.101.193.227` | 443 | ruby | monitor | 1 |
| `151.101.1.227` | 443 | ruby | monitor | 1 |
| `140.82.114.21` | 443 | node | monitor | 1 |

IPv6 destinations seen (not enforced in this profile): `2a04:4e42:200::483`, `2a04:4e42:400::483`, `2a04:4e42:600::483`, `2a04:4e42::483`

## TLS SNI (logical hosts inside TLS)

| SNI host | resolved dst IP(s) | by | events |
| :------- | :----------------- | :- | -----: |
| `results-receiver.actions.githubusercontent.com` | `140.82.114.21` | .NET TP Worker, node | 2 |
| `hosted-compute-request-orchestrator-prod-eus-02.githubapp.com` | `20.75.202.224` | hosted-compute- | 1 |
| `index.rubygems.org` | `151.101.65.227` | ruby | 1 |
| `hosted-compute-watchdog-prod-eus-02.githubapp.com` | `20.75.202.224` | provjobd2567565 | 1 |

## HTTP host headers (cleartext)

| host | sample path | by |
| :--- | :---------- | :- |
| `168.63.129.16` | `/HealthService` | python3 |
| `169.254.169.254` | `/metadata/instance?api-version=2018-02-01` | python3 |

## Filesystem activity

create: 5000

---
_Raw telemetry: `.coldstep-events.jsonl` (5,938 events) is attached to the [run artifacts](https://github.com/coldstep-io/coldstep-demo/actions/runs/27519466042)._
