# demo-output — committed coldstep digests

Real output from the demo workflows, committed so you can read it **without opening
the Actions tab** (no 404s for external visitors, no expiring artifacts).

```
demo-output/
├── v0.5.3/   current — digests captured against coldstep action @v0.5.3 (agent v0.5.3)
└── v0.4.1/   historical — digests captured against coldstep action @v0.4.1 (agent v0.4.0)
```

## How these were captured

Each workflow ran on a fresh `ubuntu-latest` GitHub-hosted runner with the coldstep
eBPF agent attached. The agent writes a raw, append-only event log
(`.coldstep-events.jsonl`) of every `exec()`, every IPv4 connect/sendmsg, every DNS
answer, and every TLS SNI / HTTP host it sees.

**coldstep renders its human-readable digest only into the GitHub Step Summary** — at
both `@v0.4.1` and `@v0.5.3` it does not write a committable `.md` file to the workspace.
So each `<version>/<pkg>.md` here is a faithful summary extracted directly from that run's
unmodified `.coldstep-events.jsonl` via [`extract-digest.py`](extract-digest.py) — the raw
telemetry is the source of truth, and the header of each file links the exact run. It
reports the same events coldstep renders, grouped the same way.

`v0.5.3/` is the current capture; `v0.4.1/` is kept for historical comparison (note how the
defend story went from "no block + red upload" at v0.4.1 to a clean green-on-block at v0.5.3).

## Files

| pkg manager | install command | v0.5.3 (current) | v0.4.1 (historical) |
| :---------- | :-------------- | :--------------- | :------------------ |
| npm   | `express`, `@aws-sdk/client-s3`          | [npm.md](v0.5.3/npm.md)   | [npm.md](v0.4.1/npm.md) |
| pip   | `pandas numpy scikit-learn matplotlib`   | [pip.md](v0.5.3/pip.md)   | [pip.md](v0.4.1/pip.md) |
| cargo | `ripgrep`                                 | [cargo.md](v0.5.3/cargo.md) | [cargo.md](v0.4.1/cargo.md) |
| go    | `golang.org/x/tools/gopls@latest`         | [go.md](v0.5.3/go.md)     | [go.md](v0.4.1/go.md) |
| apt   | `ffmpeg`                                   | [apt.md](v0.5.3/apt.md)   | [apt.md](v0.4.1/apt.md) |
| gem   | `jekyll`                                   | [gem.md](v0.5.3/gem.md)   | [gem.md](v0.4.1/gem.md) |
| defend (npm) | `express` with allowlist enforced  | [defend-npm.md](v0.5.3/defend-npm.md) | [defend-npm.md](v0.4.1/defend-npm.md) |
