# coldstep defend digest — `npm` (allowlisted)

> **Real run, fully green.** coldstep agent `v0.5.3`, action `@v0.5.3`, `mode: defend`,
> allowlist `registry.npmjs.org` + `cdn.npmjs.com`, `ignored-nets: 127.0.0.0/8`.
> Run: [27519466667](https://github.com/coldstep-io/coldstep-demo/actions/runs/27519466667) — **success**.

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

## Notes for this version

- **Clean finalization.** Unlike `@v0.4.1` (whose defend runs hung for many minutes in the
  agent's post-step), the `@v0.5.3` defend run finalized promptly and reported `success`.
- **Telemetry artifact.** In v0.5.3 defend mode the agent does not emit `.coldstep-*` files
  matching the upload glob, so the telemetry artifact for defend runs is empty — the upload step
  is intentionally non-fatal (`if-no-files-found: warn`, `continue-on-error`) so this never reds
  a correct block. The authoritative signal is the assert step above.

## The mechanism

In defend mode coldstep enforces at the cgroup `connect4` / `sendmsg4` hooks (plus BPF LSM where
available): any IPv4 destination not on the allowlist is dropped before the packet leaves. See
[`../v0.4.1/defend-npm.md`](../v0.4.1/defend-npm.md) for the history of how this showcase reached
green (express alone never triggers a block; the unauthorized `curl` makes the block
deterministic).
