# coldstep defend digest — `npm` (allowlisted)

> **Real run, fully green.** coldstep agent `v0.5.4`, action `@v0.5.4`, `mode: defend`,
> allowlist `registry.npmjs.org` + `cdn.npmjs.com` (IPv4 loopback `127.0.0.0/8` is always bypassed).
> Run: [27522186219](https://github.com/coldstep-io/coldstep-demo/actions/runs/27522186219) — **success**.

This is the green-on-block showcase: the job passes **because defend enforced the allowlist.**

## What happened

| step | what it tests | outcome | meaning |
| :--- | :------------ | :------ | :------ |
| `npm install express` | allowlisted registry traffic | `success` | ✅ defend doesn't break approved installs |
| `curl 1.1.1.1` | unauthorized egress (not on allowlist) | `failure` | ✅ **dropped at the cgroup `connect4` hook — the showcase** |
| assert block happened | green-on-block gate | `success` | ✅ job is green *because* the block occurred |

The legitimate registry traffic express needs went through untouched; the connection to
`1.1.1.1` — which is not on the allowlist — was dropped before it ever left the runner. A red
❌ on this job would mean defend *failed* to block (a real regression), not "the block worked".

## Why this digest is hand-authored (not the native digest)

v0.5.4 makes the action write a native digest to `.coldstep-<mode>.md` by default — and on this
run it *did* write `.coldstep-defend.md` on the runner. But a **defend** run still cannot upload
that file as an artifact, for two compounding reasons:

1. **Render happens in the post step.** The digest is rendered by `coldstep stop` in the action's
   node `post:` hook, which runs *after* the job's own `Upload coldstep telemetry` step — so the
   file does not yet exist when the upload runs.
2. **Defend blocks the uploader's egress.** While the agent is still enforcing, `actions/upload-artifact`'s
   own connection to GitHub's artifact service is itself non-allowlisted egress and is dropped —
   observed on this run as `Failed to CreateArtifact: connect EPERM 140.82.114.21:443`. That is
   defend doing exactly its job, on the uploader.

So for defend runs the authoritative signal remains the **assert step** above (green-on-block),
and this digest is authored from the run's observable outcome. The detect demos
(`npm.md`, `pip.md`, …) commit the native `.coldstep-detect.md` verbatim, since detect does not
block the uploader.

## The mechanism

In defend mode coldstep enforces at the cgroup `connect4` / `sendmsg4` hooks (plus `connect6` /
`sendmsg6` for IPv6, and BPF LSM where available): any destination not on the allowlist is dropped
before the packet leaves. See [`../v0.4.1/defend-npm.md`](../v0.4.1/defend-npm.md) for the history
of how this showcase reached green (express alone never triggers a block; the unauthorized `curl`
makes the block deterministic).
