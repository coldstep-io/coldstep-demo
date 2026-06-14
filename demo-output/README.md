# demo-output — committed coldstep digests

Real output from the demo workflows, committed so you can read it **without opening
the Actions tab** (no 404s for external visitors, no expiring artifacts).

```
demo-output/
├── v0.4.1/   digests captured against coldstep action @v0.4.1 (agent v0.4.0)
└── v0.5.3/   digests captured against coldstep action @v0.5.3   (added after the bump)
```

## How these were captured

Each workflow ran on a fresh `ubuntu-latest` GitHub-hosted runner with the coldstep
eBPF agent attached. The agent writes a raw, append-only event log
(`.coldstep-events.jsonl`) of every `exec()`, every IPv4 connect/sendmsg, every DNS
answer, and every TLS SNI / HTTP host it sees.

**A note on `v0.4.1/`:** at action `@v0.4.1` coldstep renders its human-readable digest
**only into the GitHub Step Summary** — it does not write a committable `.md` file. So
each `v0.4.1/<pkg>.md` here is a faithful summary extracted directly from that run's
unmodified `.coldstep-events.jsonl` (the raw telemetry is the source of truth; the
header of each file links the exact run). It reports the same events coldstep renders,
grouped the same way.

From `@v0.5.x` onward coldstep writes the rendered digest to a file directly, so
`v0.5.3/` will contain coldstep's own output verbatim — no extraction step.

## Files

| pkg manager | install command | digest |
| :---------- | :-------------- | :----- |
| npm   | `express`, `@aws-sdk/client-s3`          | [v0.4.1/npm.md](v0.4.1/npm.md) |
| pip   | `pandas numpy scikit-learn matplotlib`   | [v0.4.1/pip.md](v0.4.1/pip.md) |
| cargo | `ripgrep`                                 | [v0.4.1/cargo.md](v0.4.1/cargo.md) |
| go    | `golang.org/x/tools/gopls@latest`         | [v0.4.1/go.md](v0.4.1/go.md) |
| apt   | `ffmpeg`                                   | [v0.4.1/apt.md](v0.4.1/apt.md) |
| gem   | `jekyll`                                   | [v0.4.1/gem.md](v0.4.1/gem.md) |
| defend (npm) | `express` with allowlist enforced  | [v0.4.1/defend-npm.md](v0.4.1/defend-npm.md) |
