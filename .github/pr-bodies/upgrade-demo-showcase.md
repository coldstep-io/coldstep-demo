## Summary

Rework all seven demo workflows so each run produces a proper, shareable showcase of what `coldstep` captures — not just a smoke test that the action loads.

For every workflow:

- Drop the invalid `report: step-summary` value (the action's documented values are `job-summary` / `pr-comment` / `both` / `none`). `job-summary` is the default, so the line is removed entirely.
- Add `detect-profile: enhanced` to flip on `proc_tree`, `tls_sni`, and `fs_events` event streams.
- Add `fail-on-error: true` so the agent must reach operational readiness, otherwise the job fails loudly instead of silently producing a blind run.
- Give the action step an explicit `id: coldstep` so its outputs can be referenced.
- After the install step, a new "Suggested allowlist" step echoes `${{ steps.coldstep.outputs.suggested-allow }}` into a fenced code block in the Job Summary — copy-pastable straight into the `allow:` input for converting that workflow to defend mode.
- An `actions/upload-artifact@v4` step (`if: always()`, `include-hidden-files: true`, `retention-days: 14`) ships `.coldstep-events.jsonl`, `.coldstep-detect.md`, and `.coldstep-telemetry.json` under a per-run name. This is the path consumers will use to download the raw evidence and (once `coldstep-report-linux-amd64` is published — see coldstep-io/coldstep#219) render an HTML report.

### `defend-npm.yml` specifics

- `mode: defend` and the `allow:` list are kept exactly as-is.
- The `npm install` step now sets `continue-on-error: true` and an `id`, so its outcome can be consumed by a follow-up step.
- A "Report defend outcome" step writes to the Job Summary whether the install failed (PASS — defend mode blocked at least one non-allowlisted connection, exactly as designed) or completed (NOTE — confirm via `.coldstep-events.jsonl` that no `deny` events were emitted).
- The same artifact upload step is included, so the deny events are downloadable.

The suggested-allow step is intentionally omitted from `defend-npm.yml` since the `suggested-allow` action output is empty in defend mode.

## Files changed

- `.github/workflows/apt-install.yml`
- `.github/workflows/cargo-install.yml`
- `.github/workflows/defend-npm.yml`
- `.github/workflows/gem-install.yml`
- `.github/workflows/go-install.yml`
- `.github/workflows/npm-install.yml`
- `.github/workflows/pip-install.yml`
- `.github/pr-bodies/upgrade-demo-showcase.md` (this template)

## Test plan

- [ ] `workflow_dispatch` each of the six detect-mode workflows from the Actions tab on `main` after merge and confirm: agent reaches readiness; Job Summary shows the detect digest plus a populated "Suggested allowlist" fenced block; the per-run `coldstep-<job>-<run_id>` artifact is downloadable and contains all three files.
- [ ] `workflow_dispatch` `defend-npm.yml` and confirm: agent reaches readiness; Job Summary shows the defend outcome block; the deny events (if any) appear in the uploaded `.coldstep-events.jsonl`.
