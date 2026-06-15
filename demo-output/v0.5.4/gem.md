# coldstep detailed report

## Verdict

✅ no anomalies (IPv4 TCP/UDP in scope) · mode detect · 5824 events

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
| 168.63.129.16 | 59 |
| 127.0.0.53 | 11 |
| 127.0.0.1 | 8 |
| rubygems.org | 5 |
| blob.bn9prdstrz04a.trafficmanager.net | 3 |
| 140.82.113.24 | 1 |
| 20.150.88.228 | 1 |
| 2a04:4e42:200::483 | 1 |
| 2a04:4e42:400::483 | 1 |
| 2a04:4e42:600::483 | 1 |
| 2a04:4e42::483 | 1 |
| glb-db52c2cf8be544.github.com | 1 |

## Denies

_none_

## Process & filesystem

| stream | count |
|---|---|
| exec | 269 |
| proc_fork | 318 |
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
| IPv6 egress | 5 | non-loopback IPv6 egress events |
| QUIC/HTTP3 candidates | 0 | UDP/443 flows, payload not inspectable |
| io_uring send | 0 | async sends bypassing syscall arms |
| io_uring TLS | 0 | TLS ClientHello observed over io_uring |
| egress backstop | 0 | egress that bypassed connect4/sendmsg4 (raw socket / post-connect) |
| BPF self-defense denials | 0 | denied tamper of coldstep's own BPF objects |
| BPF audit | 87 | bpf() syscall observations |
| BPF tamper | 0 | detected BPF map/prog tamper (anti-blindness) |
| TCP state transitions | 23 | kernel-confirmed handshakes |

## BPF health

🚨 1 hook(s) failed to attach (coverage gap): raw_tp/io_uring_submit_sqe

## Integrity

parse errors: 0
