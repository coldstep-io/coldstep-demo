# coldstep detailed report

## Verdict

✅ no anomalies (IPv4 TCP/UDP in scope) · mode detect · 11127 events

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
| 168.63.129.16 | 117 |
| 127.0.0.53 | 22 |
| 127.0.0.1 | 20 |
| 142.251.219.177 | 10 |
| 142.251.219.17 | 6 |
| 169.254.169.254 | 4 |
| 142.251.218.219 | 3 |
| 142.251.219.155 | 3 |
| 2607:f8b0:4005:816::2011 | 3 |
| 142.251.214.59 | 2 |
| 142.251.218.123 | 2 |
| 142.251.218.155 | 2 |
| 142.251.218.187 | 2 |
| 142.251.218.251 | 2 |
| 142.251.218.91 | 2 |
| 142.251.219.187 | 2 |
| 142.251.219.27 | 2 |
| 142.251.219.59 | 2 |
| 2607:f8b0:4005:801::201b | 2 |
| 2607:f8b0:4005:806::2011 | 2 |
| 2607:f8b0:4005:806::201b | 2 |
| 2607:f8b0:4005:808::201b | 2 |
| 2607:f8b0:4005:809::201b | 2 |
| 140.82.113.21 | 1 |
| 20.75.202.224 | 1 |
| glb-db52c2cf8be544.github.com | 1 |

## Denies

_none_

## Process & filesystem

| stream | count |
|---|---|
| exec | 1027 |
| proc_fork | 4593 |
| fs_event | 5000 |

## TLS SNI confidence

| level | count |
|---|---|
| full | 16 |
| partial | 0 |
| inferred | 0 |
| unknown | 0 |

## Coverage & defend signals

| signal | count | meaning |
|---|---|---|
| IPv6 egress | 14 | non-loopback IPv6 egress events |
| QUIC/HTTP3 candidates | 0 | UDP/443 flows, payload not inspectable |
| io_uring send | 0 | async sends bypassing syscall arms |
| io_uring TLS | 0 | TLS ClientHello observed over io_uring |
| egress backstop | 0 | egress that bypassed connect4/sendmsg4 (raw socket / post-connect) |
| BPF self-defense denials | 0 | denied tamper of coldstep's own BPF objects |
| BPF audit | 132 | bpf() syscall observations |
| BPF tamper | 0 | detected BPF map/prog tamper (anti-blindness) |
| TCP state transitions | 59 | kernel-confirmed handshakes |

## BPF health

🚨 1 hook(s) failed to attach (coverage gap): raw_tp/io_uring_submit_sqe

## Integrity

parse errors: 0
