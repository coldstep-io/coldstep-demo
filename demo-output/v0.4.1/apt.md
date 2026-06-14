# coldstep detect digest — `apt`

> **Faithful summary of real coldstep telemetry.** Extracted from the unmodified `.coldstep-events.jsonl` produced by [this run](https://github.com/coldstep-io/coldstep-demo/actions/runs/27513830914) (coldstep agent `v0.4.0`, action `@v0.4.1`, `mode: detect`, profile `enhanced`). At v0.4.1 coldstep posts the rendered digest only to the GitHub **Step Summary**; this file summarizes the same events so you can read them here. v0.5.x writes a committable digest file directly — see `../v0.5.3/`.

**Install command:** `apt-get install ffmpeg`  
**Kernel:** `6.17.0-1018-azure`  
**Run:** [27513830914](https://github.com/coldstep-io/coldstep-demo/actions/runs/27513830914) · job `apt-demo` · sha `58dcafb`

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

1459 fork events; 918 `exec()` calls captured. Binaries executed:

- `node` → `/home/runner/actions-runner/cached/2.335.1/externals/node24/bin/node`
- `bash` → `/usr/bin/bash`
- `sudo` → `/usr/bin/sudo`
- `apt-get` → `/usr/bin/apt-get`
- `dpkg` → `/usr/bin/dpkg`
- `https` → `/usr/lib/apt/methods/https`
- `mirror+file` → `/usr/lib/apt/methods/mirror+file`
- `sh` → `/bin/sh`
- `id` → `/usr/bin/id`
- `systemctl` → `/usr/bin/systemctl`
- `9` → `/proc/self/fd/9`
- `python3` → `/usr/bin/python3`
- `file` → `/usr/lib/apt/methods/file`
- `http` → `/usr/lib/apt/methods/http`
- `gpgv` → `/usr/lib/apt/methods/gpgv`
- `apt-key` → `/usr/bin/apt-key`
- `apt-config` → `/usr/bin/apt-config`
- `ubuntu-distro-i` → `/usr/bin/ubuntu-distro-info`
- `gpgv` → `/usr/bin/gpgv`
- `mktemp` → `/usr/bin/mktemp`
- `chmod` → `/usr/bin/chmod`
- `sed` → `/usr/bin/sed`
- `gpgconf` → `/usr/bin/gpgconf`
- `gpg-connect-age` → `/usr/bin/gpg-connect-agent`
- `rm` → `/usr/bin/rm`
- `store` → `/usr/lib/apt/methods/store`
- `touch` → `/usr/bin/touch`
- `test` → `/usr/bin/test`
- `gdbus` → `/usr/bin/gdbus`
- `packagekitd` → `/usr/libexec/packagekitd`
- `echo` → `/bin/echo`
- `appstreamcli` → `/usr/bin/appstreamcli`
- `cnf-update-db` → `/usr/lib/cnf-update-db`
- `apt-helper` → `/usr/lib/apt/apt-helper`
- `update-motd-upd` → `/usr/lib/update-notifier/update-motd-updates-available`
- `find` → `/usr/bin/find`
- `dirname` → `/usr/bin/dirname`
- `apt-check` → `/usr/lib/update-notifier/apt-check`
- `mv` → `/usr/bin/mv`
- `ischroot` → `/usr/bin/ischroot`
- `dpkg-preconfigu` → `/usr/sbin/dpkg-preconfigure`
- `locale` → `/usr/bin/locale`
- `apt-extracttemp` → `/usr/bin/apt-extracttemplates`
- `sh` → `/usr/bin/sh`
- `dpkg-status` → `/usr/lib/needrestart/dpkg-status`
- `mkdir` → `/usr/bin/mkdir`
- `dpkg-split` → `/usr/bin/dpkg-split`
- `dpkg-deb` → `/usr/bin/dpkg-deb`
- `tar` → `/usr/bin/tar`
- `preinst` → `/var/lib/dpkg/tmp.ci/preinst`
- `dpkg-maintscrip` → `/usr/bin/dpkg-maintscript-helper`
- `basename` → `/usr/bin/basename`
- `libblas3:amd64.` → `/var/lib/dpkg/info/libblas3:amd64.postinst`
- `update-alternat` → `/usr/bin/update-alternatives`
- `librsvg2-common` → `/var/lib/dpkg/info/librsvg2-common:amd64.postinst`
- `dpkg-trigger` → `/usr/bin/dpkg-trigger`
- `liblapack3:amd6` → `/var/lib/dpkg/info/liblapack3:amd64.postinst`
- `libpulse0:amd64` → `/var/lib/dpkg/info/libpulse0:amd64.postinst`
- `man-db.postinst` → `/var/lib/dpkg/info/man-db.postinst`
- `libgdk-pixbuf-2` → `/var/lib/dpkg/info/libgdk-pixbuf-2.0-0:amd64.postinst`
- `sort` → `/usr/bin/sort`
- `gdk-pixbuf-quer` → `/usr/lib/x86_64-linux-gnu/gdk-pixbuf-2.0/gdk-pixbuf-query-loaders`
- `libc-bin.postin` → `/var/lib/dpkg/info/libc-bin.postinst`
- `ldconfig` → `/usr/sbin/ldconfig`
- `ldconfig.real` → `/sbin/ldconfig.real`
- `apt-pinvoke` → `/usr/lib/needrestart/apt-pinvoke`
- `dbus-send` → `/usr/bin/dbus-send`
- `needrestart` → `/usr/sbin/needrestart`
- `systemd-detect-` → `/usr/bin/systemd-detect-virt`
- `who` → `/usr/bin/who`
- `frontend` → `/usr/share/debconf/frontend`
- `python3.12` → `/usr/bin/python3.12`
- `node` → `/home/runner/actions-runner/cached/2.335.1/externals/node20/bin/node`

## IPv4 egress

Every distinct IPv4 destination the install touched (TCP connects + UDP datagrams):

| destination | port(s) | by | policy | events |
| :---------- | :------ | :- | :----- | -----: |
| `168.63.129.16` | 53,80,32526 | python3, systemd-resolve | monitor | 67 |
| `127.0.0.53` | 53 | hosted-compute-, http, https, node, provjobd3490303 | monitor | 37 |
| `127.0.0.1` | 33618,33776,36396,36751,37185,38361,39726,41453,43048,43334,49308,49757,50970,51158,51744,59103,60065 | systemd-resolve | monitor | 24 |
| `13.107.246.66` | 443 | https | monitor | 9 |
| `91.189.91.46` | 443 | https | monitor | 8 |
| `192.178.142.91` | 443 | https | monitor | 7 |
| `34.245.102.249` | 443 | https | monitor | 5 |
| `52.161.185.214` | 80 | http | monitor | 2 |
| `20.75.202.224` | 443 | hosted-compute-, provjobd3490303 | monitor | 2 |
| `13.107.213.66` | 443 | https | monitor | 1 |
| `192.178.142.136` | 443 | https | monitor | 1 |
| `192.178.142.93` | 443 | https | monitor | 1 |
| `192.178.142.190` | 443 | https | monitor | 1 |
| `34.253.181.30` | 443 | https | monitor | 1 |
| `34.244.58.147` | 443 | https | monitor | 1 |
| `3.254.173.149` | 443 | https | monitor | 1 |
| `54.154.251.197` | 443 | https | monitor | 1 |
| `185.125.190.23` | 443 | https | monitor | 1 |
| `91.189.91.47` | 443 | https | monitor | 1 |
| `185.125.190.24` | 443 | https | monitor | 1 |
| `185.125.190.75` | 443 | https | monitor | 1 |
| `140.82.112.21` | 443 | node | monitor | 1 |

IPv6 destinations seen (not enforced in this profile): `2001:67c:1562::21`, `2001:67c:1562::22`, `2607:f8b0:4023:80d::5b`, `2607:f8b0:4023:80d::5d`, `2607:f8b0:4023:80d::88`, `2607:f8b0:4023:80d::be`, `2620:1ec:46::66`, `2620:1ec:bdf::66`, `2620:2d:4000:1::2e`, `2620:2d:4000:1::2f`, `2620:2d:4000:1::30`, `2a05:d018:91c:3200:2846:99fb:81b6:1e11`, `2a05:d018:91c:3200:5e0d:21a9:26ca:90b5`, `2a05:d018:91c:3200:c887:2f22:290f:a7c`, `2a05:d018:91c:3200:c8f:1a06:a2dd:450f`, `2a05:d018:91c:3200:d8b6:37bc:63f9:703c`

## TLS SNI (logical hosts inside TLS)

| SNI host | resolved dst IP(s) | by | events |
| :------- | :----------------- | :- | -----: |
| `hosted-compute-request-orchestrator-prod-eus-01.githubapp.com` | `20.75.202.224` | hosted-compute- | 1 |
| `hosted-compute-watchdog-prod-eus-01.githubapp.com` | `20.75.202.224` | provjobd3490303 | 1 |
| `results-receiver.actions.githubusercontent.com` | `140.82.112.21` | node | 1 |

## HTTP host headers (cleartext)

| host | sample path | by |
| :--- | :---------- | :- |
| `azure.archive.ubuntu.com` | `/ubuntu/dists/noble-backports/InRelease` | http |
| `168.63.129.16` | `/machine/?comp=goalstate` | python3 |

## Filesystem activity

create: 5000

---
_Raw telemetry: `.coldstep-events.jsonl` (7,895 events) is attached to the [run artifacts](https://github.com/coldstep-io/coldstep-demo/actions/runs/27513830914)._
