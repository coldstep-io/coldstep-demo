#!/usr/bin/env bash
#
# run-demo.sh — run a coldstep demo workflow on your own machine, end to end.
#
#   ./run-demo.sh <npm|pip|cargo|go|apt|gem> [detect|defend]
#
# Examples:
#   ./run-demo.sh npm detect     # watch what `npm install` phones home
#   ./run-demo.sh npm defend     # watch defend mode block unauthorized egress
#   ./run-demo.sh go detect
#
# It runs the *exact* GitHub Actions workflow from .github/workflows/ locally,
# with the real coldstep eBPF agent, using `act` (https://github.com/nektos/act).
# Running the real workflow means there is nothing demo-specific to trust — the
# same bytes you'd get in CI, on your laptop.
#
# Requirements:
#   - Docker (a running daemon).
#   - act          https://nektosact.com  (`brew install act` / `gh extension install nektos/gh-act`)
#   - A Linux kernel with BTF + eBPF. Native Linux works out of the box; on
#     macOS/Windows, Docker Desktop's and WSL2's kernels ship BTF, so it works
#     there too. The coldstep step needs a privileged container (handled below).
#
set -euo pipefail

PKG="${1:-}"
MODE="${2:-detect}"
PIN="v0.4.1"   # coldstep action version these workflows are pinned to

die() { printf '\033[31merror:\033[0m %s\n' "$*" >&2; exit 1; }
note() { printf '\033[36m%s\033[0m\n' "$*"; }

usage() {
  sed -n '3,16p' "$0" | sed 's/^# \{0,1\}//'
  exit "${1:-0}"
}

case "$PKG" in
  -h|--help|help|"") usage 0 ;;
esac

case "$MODE" in
  detect|defend) ;;
  *) die "mode must be 'detect' or 'defend' (got '$MODE')" ;;
esac

# Map (pkg, mode) -> workflow file.
if [ "$MODE" = "defend" ]; then
  case "$PKG" in
    npm) WF="defend-npm.yml" ;;
    *)   die "defend mode currently has a demo for 'npm' only (got '$PKG'). Try: ./run-demo.sh npm defend" ;;
  esac
else
  case "$PKG" in
    npm)   WF="npm-install.yml" ;;
    pip)   WF="pip-install.yml" ;;
    cargo) WF="cargo-install.yml" ;;
    go)    WF="go-install.yml" ;;
    apt)   WF="apt-install.yml" ;;
    gem)   WF="gem-install.yml" ;;
    *)     die "unknown package manager '$PKG' (npm|pip|cargo|go|apt|gem)" ;;
  esac
fi

ROOT="$(cd "$(dirname "$0")" && pwd)"
WF_PATH="$ROOT/.github/workflows/$WF"
[ -f "$WF_PATH" ] || die "workflow not found: $WF_PATH"

# --- preflight ---------------------------------------------------------------
command -v docker >/dev/null 2>&1 || die "docker not found. Install Docker and start the daemon."
docker info >/dev/null 2>&1 || die "the Docker daemon isn't reachable. Start Docker Desktop / dockerd and retry."

ACT=""
if command -v act >/dev/null 2>&1; then
  ACT="act"
elif gh extension list 2>/dev/null | grep -q 'nektos/gh-act'; then
  ACT="gh act"
fi
if [ -z "$ACT" ]; then
  cat >&2 <<EOF
error: 'act' is required to run the workflow locally.

  Install one of:
    brew install act                       # macOS / Linuxbrew
    gh extension install nektos/gh-act     # via GitHub CLI
    https://nektosact.com/installation/    # other platforms

  Or use the bundled privileged container instead:
    docker compose run --rm coldstep-demo ./run-demo.sh $PKG $MODE
EOF
  exit 1
fi

# A runner image with the tooling the workflows expect (node, python, etc.).
IMAGE="${ACT_RUNNER_IMAGE:-catthehacker/ubuntu:full-24.04}"

note "coldstep demo  ·  pkg=$PKG  mode=$MODE  workflow=$WF  action=@$PIN"
note "running the real workflow locally via '$ACT' (privileged, image=$IMAGE)…"
echo

# The coldstep eBPF agent needs a privileged container with access to the
# kernel's BTF and tracefs. --privileged plus these mounts cover both.
set -x
$ACT workflow_dispatch \
  -W "$WF_PATH" \
  -P "ubuntu-latest=$IMAGE" \
  --privileged \
  --container-options "--privileged -v /sys/kernel/btf:/sys/kernel/btf:ro -v /sys/kernel/debug:/sys/kernel/debug:rw" \
  "$@"
status=$?
set +x

# --- show the bytes ----------------------------------------------------------
echo
DIGEST="$ROOT/.coldstep-detect.md"
if [ -s "$DIGEST" ]; then
  note "==== coldstep digest ($DIGEST) ===="
  cat "$DIGEST"
else
  note "Digest was written to the job's Step Summary (act prints it inline above)."
  note "At action @$PIN coldstep does not write a standalone digest file; see the"
  note "'Suggested allowlist' / 'Defend mode showcase' blocks in the output above,"
  note "and demo-output/$PIN/$PKG.md in this repo for a committed capture."
fi

exit $status
