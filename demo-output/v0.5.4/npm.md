# coldstep detailed report

## Verdict

✅ no anomalies (IPv4 TCP/UDP in scope) · mode detect · 5315 events

agent v0.5.4 · kernel 6.17.0-1018-azure · profile enhanced · allowlist 0 IP(s) / 0 entr(ies)

## Coverage scope

| class | status |
|---|---|
| IPv4 TCP/UDP | observed |
| IPv6 | observed |
| QUIC/HTTP3 | not observed |

## Destinations

| destination | egress events |
|---|---|
| registry.npmjs.org | 54 |
| 168.63.129.16 | 13 |
| 127.0.0.53 | 9 |
| 127.0.0.1 | 6 |
| 2606:4700::6810:122 | 2 |
| 2606:4700::6810:22 | 2 |
| 2606:4700::6810:222 | 2 |
| 2606:4700::6810:322 | 2 |
| 2606:4700::6810:422 | 2 |
| 2606:4700::6810:522 | 2 |
| 2606:4700::6810:622 | 2 |
| 2606:4700::6810:722 | 2 |
| 2606:4700::6810:822 | 2 |
| 2606:4700::6810:922 | 2 |
| 2606:4700::6810:a22 | 2 |
| 2606:4700::6810:b22 | 2 |
| glb-db52c2cf8be544.github.com | 1 |

## Denies

_none_

## Process & filesystem

| stream | count |
|---|---|
| exec | 8 |
| proc_fork | 61 |
| fs_event | 5000 |

## TLS SNI confidence

| level | count |
|---|---|
| full | 31 |
| partial | 0 |
| inferred | 0 |
| unknown | 0 |

## Coverage & defend signals

| signal | count | meaning |
|---|---|---|
| IPv6 egress | 24 | non-loopback IPv6 egress events |
| QUIC/HTTP3 candidates | 0 | UDP/443 flows, payload not inspectable |
| io_uring send | 0 | async sends bypassing syscall arms |
| io_uring TLS | 0 | TLS ClientHello observed over io_uring |
| egress backstop | 0 | egress that bypassed connect4/sendmsg4 (raw socket / post-connect) |
| BPF self-defense denials | 0 | denied tamper of coldstep's own BPF objects |
| BPF audit | 36 | bpf() syscall observations |
| BPF tamper | 0 | detected BPF map/prog tamper (anti-blindness) |
| TCP state transitions | 35 | kernel-confirmed handshakes |

## BPF health

🚨 1 hook(s) failed to attach (coverage gap): raw_tp/io_uring_submit_sqe

## Integrity

parse errors: 0
