# coldstep detect digest — `cargo`

> **Faithful summary of real coldstep telemetry.** Extracted from the unmodified `.coldstep-events.jsonl` produced by [this run](https://github.com/coldstep-io/coldstep-demo/actions/runs/27513829891) (coldstep agent `v0.4.0`, action `@v0.4.1`, `mode: detect`, profile `enhanced`). coldstep posts the rendered digest to the GitHub **Step Summary**; this file summarizes the same events so you can read them here without opening Actions. The raw telemetry is the source of truth — linked at the bottom.

**Install command:** `cargo install ripgrep`  
**Kernel:** `6.17.0-1018-azure`  
**Run:** [27513829891](https://github.com/coldstep-io/coldstep-demo/actions/runs/27513829891) · job `cargo-demo` · sha `58dcafb`

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

876 fork events; 104 `exec()` calls captured. Binaries executed:

- `node` → `/home/runner/actions-runner/cached/2.335.1/externals/node24/bin/node`
- `bash` → `/usr/bin/bash`
- `cargo` → `/home/runner/.cargo/bin/cargo`
- `cargo` → `/home/runner/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/bin/cargo`
- `rustc` → `/home/runner/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/bin/rustc`
- `cc` → `/usr/bin/cc`
- `collect2` → `/usr/libexec/gcc/x86_64-linux-gnu/13/collect2`
- `ld.lld` → `/home/runner/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/lib/rustlib/x86_64-unknown-linux-gnu/bin/gcc-ld/ld.lld`
- `rust-lld` → `/home/runner/.rustup/toolchains/stable-x86_64-unknown-linux-gnu/lib/rustlib/x86_64-unknown-linux-gnu/bin/rust-lld`
- `build-script-bu` → `/tmp/cargo-installCDwkIH/release/build/libc-39b7c4687f3e8ad9/build-script-build`
- `build-script-bu` → `/tmp/cargo-installCDwkIH/release/build/serde_core-6e90c9cdc5815a65/build-script-build`
- `build-script-bu` → `/tmp/cargo-installCDwkIH/release/build/zmij-ec2b159e7f80e5ba/build-script-build`
- `build-script-bu` → `/tmp/cargo-installCDwkIH/release/build/crossbeam-utils-64d555677845c7b4/build-script-build`
- `build-script-bu` → `/tmp/cargo-installCDwkIH/release/build/serde-b4582a7719eb0313/build-script-build`
- `build-script-bu` → `/tmp/cargo-installCDwkIH/release/build/serde_json-3884c0cec065e538/build-script-build`
- `build-script-bu` → `/tmp/cargo-installCDwkIH/release/build/anyhow-a2d1166fa017e45a/build-script-build`
- `build-script-bu` → `/tmp/cargo-installCDwkIH/release/build/ripgrep-eab4f90a14af7da4/build-script-build`
- `git` → `/usr/bin/git`
- `node` → `/home/runner/actions-runner/cached/2.335.1/externals/node20/bin/node`

## IPv4 egress

Every distinct IPv4 destination the install touched (TCP connects + UDP datagrams):

| destination | port(s) | by | policy | events |
| :---------- | :------ | :- | :----- | -----: |
| `151.101.42.137` | 443 | cargo | monitor | 189 |
| `168.63.129.16` | 53,80,32526 | python3, systemd-resolve | monitor | 67 |
| `127.0.0.53` | 53 | cargo, hosted-compute-, node | monitor | 14 |
| `127.0.0.1` | 34136,38633,40350,42843,55576,58165 | systemd-resolve | monitor | 10 |
| `20.75.202.224` | 443 | hosted-compute- | monitor | 1 |
| `140.82.114.22` | 443 | node | monitor | 1 |

IPv6 destinations seen (not enforced in this profile): `2a04:4e42:2f::649`, `2a04:4e42:a::649`

## TLS SNI (logical hosts inside TLS)

| SNI host | resolved dst IP(s) | by | events |
| :------- | :----------------- | :- | -----: |
| `static.crates.io` | `151.101.42.137` | cargo | 2 |
| `index.crates.io` | `151.101.42.137` | cargo | 1 |
| `hosted-compute-request-orchestrator-prod-eus-02.githubapp.com` | `20.75.202.224` | hosted-compute- | 1 |
| `results-receiver.actions.githubusercontent.com` | `140.82.114.22` | node | 1 |

## HTTP host headers (cleartext)

| host | sample path | by |
| :--- | :---------- | :- |
| `168.63.129.16` | `/machine/?comp=goalstate` | python3 |

## Filesystem activity

create: 5000

---
_Raw telemetry: `.coldstep-events.jsonl` (6,604 events) is attached to the [run artifacts](https://github.com/coldstep-io/coldstep-demo/actions/runs/27513829891)._
