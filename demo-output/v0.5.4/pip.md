# coldstep detailed report

## Verdict

✅ no anomalies (IPv4 TCP/UDP in scope) · mode detect · 5288 events

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
| 168.63.129.16 | 47 |
| 127.0.0.53 | 11 |
| pypi.org | 10 |
| 127.0.0.1 | 8 |
| 2a04:4e42:200::223 | 2 |
| 2a04:4e42:400::223 | 2 |
| 2a04:4e42:600::223 | 2 |
| 2a04:4e42::223 | 2 |
| 140.82.114.23 | 1 |
| glb-db52c2cf8be544.github.com | 1 |

## Denies

_none_

## Process & filesystem

| stream | count |
|---|---|
| exec | 15 |
| proc_fork | 77 |
| fs_event | 5000 |

## TLS SNI confidence

| level | count |
|---|---|
| full | 4 |
| partial | 0 |
| inferred | 0 |
| unknown | 0 |

## Coverage & defend signals

| signal | count | meaning |
|---|---|---|
| IPv6 egress | 8 | non-loopback IPv6 egress events |
| QUIC/HTTP3 candidates | 0 | UDP/443 flows, payload not inspectable |
| io_uring send | 0 | async sends bypassing syscall arms |
| io_uring TLS | 0 | TLS ClientHello observed over io_uring |
| egress backstop | 0 | egress that bypassed connect4/sendmsg4 (raw socket / post-connect) |
| BPF self-defense denials | 0 | denied tamper of coldstep's own BPF objects |
| BPF audit | 61 | bpf() syscall observations |
| BPF tamper | 0 | detected BPF map/prog tamper (anti-blindness) |
| TCP state transitions | 20 | kernel-confirmed handshakes |

## BPF health

🚨 1 hook(s) failed to attach (coverage gap): raw_tp/io_uring_submit_sqe

## Integrity

parse errors: 0
