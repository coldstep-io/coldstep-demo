# coldstep detect digest — `go`

> **Faithful summary of real coldstep telemetry.** Extracted from the unmodified `.coldstep-events.jsonl` produced by [this run](https://github.com/coldstep-io/coldstep-demo/actions/runs/27519464642) (coldstep agent `v0.5.3`, action `@v0.5.3`, `mode: detect`, profile `enhanced`). coldstep posts the rendered digest to the GitHub **Step Summary**; this file summarizes the same events so you can read them here without opening Actions. The raw telemetry is the source of truth — linked at the bottom.

**Install command:** `go install golang.org/x/tools/gopls@latest`  
**Kernel:** `6.17.0-1018-azure`  
**Run:** [27519464642](https://github.com/coldstep-io/coldstep-demo/actions/runs/27519464642) · job `go-demo` · sha `a7ecac0`

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

4532 fork events; 1007 `exec()` calls captured. Binaries executed:

- `node` → `/home/runner/actions-runner/extracted/externals/node24/bin/node`
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
- `link` → `/home/runner/go/pkg/mod/golang.org/toolchain@v0.0.1-go1.26.4.linux-amd64/pkg/tool/linux_amd64/link`
- `node` → `/home/runner/actions-runner/extracted/externals/node20/bin/node`

## IPv4 egress

Every distinct IPv4 destination the install touched (TCP connects + UDP datagrams):

| destination | port(s) | by | policy | events |
| :---------- | :------ | :- | :----- | -----: |
| `168.63.129.16` | 53,80,32526 | python3, systemd-resolve | monitor | 98 |
| `127.0.0.53` | 53 | .NET TP Worker, go, node | monitor | 23 |
| `127.0.0.1` | 33950,34293,35209,36389,40830,43003,43233,44193,44682,48115,50070,51270,52542,54525,56194,57611,58286 | systemd-resolve | monitor | 20 |
| `173.194.45.141` | 53,443 | go | monitor | 10 |
| `172.253.62.141` | 53,443 | go | monitor | 6 |
| `142.251.111.207` | 53,443 | go | monitor | 3 |
| `142.251.163.207` | 53,443 | go | monitor | 3 |
| `142.251.16.207` | 53 | go | monitor | 2 |
| `142.251.167.207` | 53 | go | monitor | 2 |
| `192.178.155.207` | 53 | go | monitor | 2 |
| `173.194.45.207` | 53 | go | monitor | 2 |
| `142.251.179.207` | 53 | go | monitor | 2 |
| `172.253.62.207` | 53 | go | monitor | 2 |
| `172.253.122.207` | 53 | go | monitor | 2 |
| `172.253.63.207` | 53 | go | monitor | 2 |
| `169.254.169.254` | 80 | python3 | monitor | 2 |
| `20.209.226.129` | 0 | .NET TP Worker | monitor | 1 |
| `20.209.226.1` | 0 | .NET TP Worker | monitor | 1 |
| `20.209.227.33` | 0 | .NET TP Worker | monitor | 1 |
| `140.82.112.22` | 443 | node | monitor | 1 |

IPv6 destinations seen (not enforced in this profile): `2607:f8b0:4004:c06::cf`, `2607:f8b0:4004:c07::cf`, `2607:f8b0:4004:c08::cf`, `2607:f8b0:4004:c0b::8d`, `2607:f8b0:4004:c0b::cf`, `2607:f8b0:4004:c29::8d`

## TLS SNI (logical hosts inside TLS)

| SNI host | resolved dst IP(s) | by | events |
| :------- | :----------------- | :- | -----: |
| `proxy.golang.org` | `173.194.45.141` | go | 8 |
| `sum.golang.org` | `172.253.62.141` | go | 3 |
| `results-receiver.actions.githubusercontent.com` | `140.82.112.22` | .NET TP Worker, node | 2 |
| `storage.googleapis.com` | `142.251.111.207`, `142.251.163.207` | go | 2 |
| `productionresultssa12.blob.core.windows.net` | `20.209.226.129` | .NET TP Worker | 1 |

## HTTP host headers (cleartext)

| host | sample path | by |
| :--- | :---------- | :- |
| `168.63.129.16` | `/HealthService` | python3 |
| `169.254.169.254` | `/metadata/instance?api-version=2018-02-01` | python3 |

## Filesystem activity

create: 5000

---
_Raw telemetry: `.coldstep-events.jsonl` (11,008 events) is attached to the [run artifacts](https://github.com/coldstep-io/coldstep-demo/actions/runs/27519464642)._
