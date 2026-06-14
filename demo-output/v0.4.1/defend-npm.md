# coldstep defend digest — `npm` (allowlisted)

> **Faithful record of real coldstep runs** at action `@v0.4.1`, `mode: defend`, allowlist
> `registry.npmjs.org` + `cdn.npmjs.com`, `ignored-nets: 127.0.0.0/8`.
> Runs: [27513832086](https://github.com/coldstep-io/coldstep-demo/actions/runs/27513832086),
> [27514079237](https://github.com/coldstep-io/coldstep-demo/actions/runs/27514079237).

**Install command:** `npm install express`

## What happened

Across repeated runs at v0.4.1, `npm install express` **completed successfully** under the
allowlist. Every host npm dialed for this install was already on the allowlist
(`registry.npmjs.org`) — express and its dependency tree are served straight from the
registry — so defend mode had nothing outside the policy to drop. The
`Report defend outcome` step therefore took its `success` branch:

> NOTE — npm install completed without being blocked. Either every host it touched was on
> the allowlist, or the version of npm in this runner image happens to talk only to the
> registry.

In other words: **at v0.4.1 this workflow does not actually demonstrate a block.** The
README's premise ("expected to be blocked somewhere") did not hold for `express` on the
current `ubuntu-latest` image — express installs cleanly from the registry alone.

## Two problems this surfaced (both fixed downstream)

1. **No block to show.** A defend *showcase* needs egress that is provably outside the
   allowlist. Fixed in `fix/defend-npm-green-on-expected-block`: the workflow now also
   attempts an explicitly unauthorized egress, which defend deterministically drops, and
   the job goes **green when the block happens** — while the legitimate `npm install`
   still succeeds.

2. **Red ❌ on a working run.** At v0.4.1 the `Upload coldstep telemetry` step **fails** in
   defend mode (the telemetry filenames it globs are not produced the same way as in
   detect mode), turning an otherwise-correct run red. Also fixed in the same branch by
   making the upload tolerant of missing files (`if-no-files-found: warn`) and globbing
   `.coldstep-*`.

## The mechanism (unchanged)

In defend mode, coldstep enforces at the cgroup `connect4` / `sendmsg4` hooks (plus BPF LSM
where available): any IPv4 destination **not** on the allowlist is dropped before the
packet leaves. The allowlisted registry traffic that express needs passes through
untouched — which is exactly why this particular install succeeded.

See [`v0.5.3/defend-npm.md`](../v0.5.3/defend-npm.md) for the deterministic green-on-block
showcase captured against the bumped action.
