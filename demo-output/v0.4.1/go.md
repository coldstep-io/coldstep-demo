# coldstep detect digest — `go`

> **Faithful summary of real coldstep telemetry.** Extracted from the unmodified `.coldstep-events.jsonl` produced by [this run](https://github.com/coldstep-io/coldstep-demo/actions/runs/27513830374) (coldstep agent `v0.4.0`, action `@v0.4.1`, `mode: detect`, profile `enhanced`). coldstep posts the rendered digest to the GitHub **Step Summary**; this file summarizes the same events so you can read them here without opening Actions. The raw telemetry is the source of truth — linked at the bottom.

**Install command:** `go install golang.org/x/tools/gopls@latest`  
**Kernel:** `6.17.0-1018-azure`  
**Run:** [27513830374](https://github.com/coldstep-io/coldstep-demo/actions/runs/27513830374) · job `go-demo` · sha `58dcafb`

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

4502 fork events; 1010 `exec()` calls captured. Binaries executed:

- `node` → `/home/runner/actions-runner/cached/2.335.1/externals/node24/bin/node`
- `bash` → `/usr/bin/bash`
- `go` → `/usr/bin/go`
- `go` → `/home/runner/go/pkg/mod/golang.org/toolchain@v0.0.1-go1.26.4.linux-amd64/bin/go`
- `compile` → `/home/runner/go/pkg/mod/golang.org/toolchain@v0.0.1-go1.26.4.linux-amd64/pkg/tool/linux_amd64/compile`
- `asm` → `/home/runner/go/pkg/mod/golang.org/toolchain@v0.0.1-go1.26.4.linux-amd64/pkg/tool/linux_amd64/asm`
- `cgo` → `/home/runner/go/pkg/mod/golang.org/toolchain@v0.0.1-go1.26.4.linux-amd64/pkg/tool/linux_amd64/cgo`
- `gcc` → `/usr/bin/gcc`
- `cc1` → `/usr/libexec/gcc/x86_64-linux-gnu/13/cc1`
- `as` → `/usr/bin/as`
- `collect2` → `/usr/libexec/gcc/x86_64-linux-gnu/13/collect2`
- `ld` → `/usr/bin/ld`
- `9` → `/proc/self/fd/9`
- `sa1` → `/usr/lib/sysstat/sa1`
- `sadc` → `/usr/lib/sysstat/sadc`
- `link` → `/home/runner/go/pkg/mod/golang.org/toolchain@v0.0.1-go1.26.4.linux-amd64/pkg/tool/linux_amd64/link`
- `node` → `/home/runner/actions-runner/cached/2.335.1/externals/node20/bin/node`

## IPv4 egress

Every distinct IPv4 destination the install touched (TCP connects + UDP datagrams):

| destination | port(s) | by | policy | events |
| :---------- | :------ | :- | :----- | -----: |
| `168.63.129.16` | 53,80,32526 | python3, systemd-resolve | monitor | 97 |
| `127.0.0.53` | 53 | go, node, provjobd3415655 | monitor | 19 |
| `127.0.0.1` | 34865,37798,38788,41234,41247,43186,43342,44854,45493,45593,46723,52719,54401,56484,57668,59961,60116 | systemd-resolve | monitor | 18 |
| `142.251.218.145` | 53,443 | go | monitor | 10 |
| `142.251.218.113` | 53,443 | go | monitor | 6 |
| `142.251.219.27` | 53,443 | go | monitor | 3 |
| `142.251.214.59` | 53,443 | go | monitor | 3 |
| `142.251.218.91` | 53 | go | monitor | 2 |
| `142.251.218.123` | 53 | go | monitor | 2 |
| `142.251.218.155` | 53 | go | monitor | 2 |
| `142.251.218.251` | 53 | go | monitor | 2 |
| `142.251.218.187` | 53 | go | monitor | 2 |
| `142.251.219.187` | 53 | go | monitor | 2 |
| `142.251.219.59` | 53 | go | monitor | 2 |
| `142.251.218.219` | 53 | go | monitor | 2 |
| `142.251.219.155` | 53 | go | monitor | 2 |
| `169.254.169.254` | 80 | python3 | monitor | 2 |
| `20.75.202.224` | 443 | provjobd3415655 | monitor | 1 |
| `140.82.112.22` | 443 | node | monitor | 1 |

IPv6 destinations seen (not enforced in this profile): `2607:f8b0:4005:80a::2011`, `2607:f8b0:4005:80a::201b`, `2607:f8b0:4005:80b::201b`, `2607:f8b0:4005:817::201b`, `2607:f8b0:4005:818::2011`, `2607:f8b0:4005:819::201b`

## TLS SNI (logical hosts inside TLS)

| SNI host | resolved dst IP(s) | by | events |
| :------- | :----------------- | :- | -----: |
| `proxy.golang.org` | `142.251.218.145` | go | 8 |
| `sum.golang.org` | `142.251.218.113` | go | 3 |
| `storage.googleapis.com` | `142.251.214.59`, `142.251.219.27` | go | 2 |
| `hosted-compute-watchdog-prod-eus-02.githubapp.com` | `20.75.202.224` | provjobd3415655 | 1 |
| `results-receiver.actions.githubusercontent.com` | `140.82.112.22` | node | 1 |

## HTTP host headers (cleartext)

| host | sample path | by |
| :--- | :---------- | :- |
| `168.63.129.16` | `/HealthService` | python3 |
| `169.254.169.254` | `/metadata/instance?api-version=2018-02-01` | python3 |

## Filesystem activity

create: 5000

---
_Raw telemetry: `.coldstep-events.jsonl` (10,956 events) is attached to the [run artifacts](https://github.com/coldstep-io/coldstep-demo/actions/runs/27513830374)._
