# coldstep detailed report

## Verdict

✅ no anomalies (IPv4 TCP/UDP in scope) · mode detect · 6605 events

agent v0.5.4 · kernel 6.17.0-1018-azure · profile enhanced · allowlist 0 IP(s) / 0 entr(ies)

## Coverage scope

| class | status |
|---|---|
| IPv4 TCP/UDP | observed |
| IPv6 | observed |
| QUIC/HTTP3 | 183 candidate(s), not inspected |

## Destinations

| destination | egress events |
|---|---|
| dualstack.k.sni.global.fastly.net | 189 |
| 168.63.129.16 | 56 |
| 127.0.0.53 | 16 |
| 127.0.0.1 | 12 |
| 2a04:4e42:87::649 | 4 |
| 169.254.169.254 | 2 |
| 20.75.202.224 | 2 |
| 2a04:4e42:2f::649 | 2 |
| glb-db52c2cf8be544.github.com | 1 |

## Denies

_none_

## Process & filesystem

| stream | count |
|---|---|
| exec | 104 |
| proc_fork | 874 |
| fs_event | 5000 |

## TLS SNI confidence

| level | count |
|---|---|
| full | 6 |
| partial | 0 |
| inferred | 0 |
| unknown | 0 |

## Coverage & defend signals

| signal | count | meaning |
|---|---|---|
| IPv6 egress | 6 | non-loopback IPv6 egress events |
| QUIC/HTTP3 candidates | 183 | UDP/443 flows, payload not inspectable |
| io_uring send | 0 | async sends bypassing syscall arms |
| io_uring TLS | 0 | TLS ClientHello observed over io_uring |
| egress backstop | 0 | egress that bypassed connect4/sendmsg4 (raw socket / post-connect) |
| BPF self-defense denials | 0 | denied tamper of coldstep's own BPF objects |
| BPF audit | 94 | bpf() syscall observations |
| BPF tamper | 0 | detected BPF map/prog tamper (anti-blindness) |
| TCP state transitions | 25 | kernel-confirmed handshakes |

## BPF health

🚨 1 hook(s) failed to attach (coverage gap): raw_tp/io_uring_submit_sqe

## Integrity

parse errors: 0
