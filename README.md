# coldstep-demo

See exactly what popular package managers phone home to — using [coldstep](https://github.com/coldstep-io/coldstep).

Every workflow in this repo runs a single install command (`npm install`, `pip install`, `cargo install`, etc.) on a fresh `ubuntu-latest` runner with the **coldstep** eBPF agent attached in `detect` mode. The shutdown digest — every process spawned, every IPv4 destination contacted, every DNS lookup — is published to that run's **Step Summary**.

Pinned to [`coldstep-io/coldstep@v0.4.0`](https://github.com/coldstep-io/coldstep/releases/tag/v0.4.0).

## The workflows

| Workflow | What it installs | Latest runs |
| :------- | :--------------- | :---------- |
| [npm install](.github/workflows/npm-install.yml) | `express`, `@aws-sdk/client-s3` | [Actions](https://github.com/coldstep-io/coldstep-demo/actions/workflows/npm-install.yml) |
| [pip install](.github/workflows/pip-install.yml) | `pandas`, `numpy`, `scikit-learn`, `matplotlib` | [Actions](https://github.com/coldstep-io/coldstep-demo/actions/workflows/pip-install.yml) |
| [cargo install](.github/workflows/cargo-install.yml) | `ripgrep` | [Actions](https://github.com/coldstep-io/coldstep-demo/actions/workflows/cargo-install.yml) |
| [go install](.github/workflows/go-install.yml) | `golang.org/x/tools/gopls@latest` | [Actions](https://github.com/coldstep-io/coldstep-demo/actions/workflows/go-install.yml) |
| [apt-get install](.github/workflows/apt-install.yml) | `ffmpeg` | [Actions](https://github.com/coldstep-io/coldstep-demo/actions/workflows/apt-install.yml) |
| [gem install](.github/workflows/gem-install.yml) | `jekyll` | [Actions](https://github.com/coldstep-io/coldstep-demo/actions/workflows/gem-install.yml) |
| [defend mode — npm allowlisted](.github/workflows/defend-npm.yml) | `express` (with allowlist enforced) | [Actions](https://github.com/coldstep-io/coldstep-demo/actions/workflows/defend-npm.yml) |

All scheduled workflows run weekly (Monday mornings, UTC) so the picture stays current as the ecosystems shift. Each one is also `workflow_dispatch`-able from the Actions tab.

## What the digest looks like

> See the latest run in the [Actions tab](https://github.com/coldstep-io/coldstep-demo/actions) — every run posts its full digest to the Step Summary.

A typical detect-mode digest contains:

- **Processes:** every `exec()` chain the install triggered (npm → node → `node-gyp` → `cc1` → linker, etc.).
- **IPv4 egress:** every destination contacted, grouped by domain (with rDNS), with byte counts.
- **DNS:** every name resolved, with answer IPs.
- **TLS SNI / HTTP host headers:** which logical hosts were addressed inside the TLS sessions.
- **BPF program health:** load status of each probe, telling you the digest isn't blind.

## detect vs defend

**`mode: detect`** (default) — observe-only. The agent records everything; nothing is blocked. Use this to *discover* what a build actually contacts before you write an allowlist.

**`mode: defend`** — IPv4 egress not on the allowlist is blocked at the cgroup `connect4`/`sendmsg4` hook (plus BPF LSM where available). Use this once you know what the build legitimately needs. See [`defend-npm.yml`](.github/workflows/defend-npm.yml) for a minimal example that allows only the npm registry.

## Use coldstep in your own workflows

```yaml
- uses: coldstep-io/coldstep@v0.4.0
  with:
    mode: detect
    report: step-summary
```

Full input reference, defend-mode setup, IPv4 scope and limits, and the agent architecture are documented at **[coldstep-io/coldstep](https://github.com/coldstep-io/coldstep)**.
