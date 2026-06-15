# coldstep detailed report

## Verdict

✅ no anomalies (IPv4 TCP/UDP in scope) · mode detect · 7898 events

agent v0.5.4 · kernel 6.17.0-1018-azure · profile enhanced · allowlist 0 IP(s) / 0 entr(ies)

## Coverage scope

| class | status |
|---|---|
| IPv4 TCP/UDP | observed |
| IPv6 | observed |
| QUIC/HTTP3 | 21 candidate(s), not inspected |

## Destinations

| destination | egress events |
|---|---|
| 168.63.129.16 | 74 |
| 127.0.0.53 | 37 |
| 127.0.0.1 | 24 |
| esm.ubuntu.com | 12 |
| 13.107.213.71 | 9 |
| motd.ubuntu.com | 9 |
| dl.google.com | 7 |
| 20.75.202.224 | 2 |
| cloud-mirror-lb.westus3.cloudapp.azure.com | 2 |
| 13.107.246.71 | 1 |
| 2001:67c:1562::21 | 1 |
| 2001:67c:1562::22 | 1 |
| 2607:f8b0:4007:807::200e | 1 |
| 2620:1ec:46::71 | 1 |
| 2620:1ec:bdf::71 | 1 |
| 2620:2d:4000:1::2e | 1 |
| 2620:2d:4000:1::2f | 1 |
| 2620:2d:4000:1::30 | 1 |
| 2a05:d018:91c:3200:2846:99fb:81b6:1e11 | 1 |
| 2a05:d018:91c:3200:5e0d:21a9:26ca:90b5 | 1 |
| 2a05:d018:91c:3200:c887:2f22:290f:a7c | 1 |
| 2a05:d018:91c:3200:c8f:1a06:a2dd:450f | 1 |
| 2a05:d018:91c:3200:d8b6:37bc:63f9:703c | 1 |
| glb-db52c2cf8be544.github.com | 1 |

## Denies

_none_

## Process & filesystem

| stream | count |
|---|---|
| exec | 918 |
| proc_fork | 1461 |
| fs_event | 5000 |

## TLS SNI confidence

| level | count |
|---|---|
| full | 3 |
| partial | 0 |
| inferred | 0 |
| unknown | 0 |

## Coverage & defend signals

| signal | count | meaning |
|---|---|---|
| IPv6 egress | 13 | non-loopback IPv6 egress events |
| QUIC/HTTP3 candidates | 21 | UDP/443 flows, payload not inspectable |
| io_uring send | 0 | async sends bypassing syscall arms |
| io_uring TLS | 0 | TLS ClientHello observed over io_uring |
| egress backstop | 0 | egress that bypassed connect4/sendmsg4 (raw socket / post-connect) |
| BPF self-defense denials | 0 | denied tamper of coldstep's own BPF objects |
| BPF audit | 107 | bpf() syscall observations |
| BPF tamper | 0 | detected BPF map/prog tamper (anti-blindness) |
| TCP state transitions | 29 | kernel-confirmed handshakes |

## BPF health

🚨 1 hook(s) failed to attach (coverage gap): raw_tp/io_uring_submit_sqe

## Integrity

parse errors: 0
