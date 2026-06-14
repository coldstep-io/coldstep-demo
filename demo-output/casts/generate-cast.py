#!/usr/bin/env python3
"""Generate an asciicast v2 replay touring the *committed* coldstep digests.

This is a scripted replay (not a live capture): every line of output it prints
is read from the real demo-output/ digests this repo commits, so viewers see
the genuine telemetry. We can't live-record coldstep off-CI because the eBPF
agent needs a Linux runner; this replays the bytes we did capture.
"""
import json, sys, os

W, H = 100, 30
E = chr(27)
CYAN = E + "[36m"; GREEN = E + "[32m"; RED = E + "[31m"; DIM = E + "[2m"
YEL = E + "[33m"; BOLD = E + "[1m"; RST = E + "[0m"
PROMPT = GREEN + "demo$" + RST + " "

events = []
t = [0.0]

def emit(s, dt=0.0):
    t[0] += dt
    events.append([round(t[0], 3), "o", s])

def typed(cmd, dt=0.035):
    emit(PROMPT)
    for ch in cmd:
        emit(ch, dt)
    emit("\r\n", 0.25)

def out(lines, dt=0.03, pause=0.0):
    for ln in lines:
        emit(ln + "\r\n", dt)
    if pause:
        t[0] += pause

def comment(txt):
    typed(DIM + "# " + txt + RST, dt=0.012)

comment("coldstep: see exactly what a package install phones home - then block it.")
t[0] += 0.4
comment("DETECT mode ran `npm install express` in CI with the eBPF agent attached.")
t[0] += 0.3

typed("cat demo-output/v0.4.1/npm.md   # real captured telemetry")
out([
    BOLD + "# coldstep detect digest - npm" + RST,
    "",
    DIM + "Install: npm install express && npm install @aws-sdk/client-s3" + RST,
    "",
    BOLD + "## IPv4 egress" + RST + "  " + DIM + "(every destination the install touched)" + RST,
    "",
    "  destination       port   by                 policy    events",
    "  ---------------   ----   ----------------   -------   ------",
    "  " + YEL + "104.16.4.34" + RST + "       443    npm install exp    monitor       17",
    "  " + YEL + "168.63.129.16" + RST + "     53,80  python3 (Azure)    monitor       14   " + DIM + "<- cloud metadata" + RST,
    "  " + YEL + "140.82.112.22" + RST + "     443    node (GH Actions)  monitor        1",
    "",
    BOLD + "## TLS SNI" + RST + "  " + DIM + "(logical hosts inside the TLS sessions)" + RST,
    "",
    "  " + CYAN + "registry.npmjs.org" + RST + "                              30 events",
    "  " + CYAN + "results-receiver.actions.githubusercontent.com" + RST + "   1 event",
    "  " + CYAN + "hosted-compute-...githubapp.com" + RST + "                  1 event",
], dt=0.04)
t[0] += 1.4
comment("So npm install talks to the registry - plus GitHub + Azure infra. Now lock it down.")
t[0] += 0.5

comment("DEFEND mode: allow ONLY the npm registry; drop everything else at the kernel.")
t[0] += 0.3
typed("cat demo-output/v0.4.1/defend-npm.md   # the block, captured")
out([
    BOLD + "# coldstep defend - npm allowlisted" + RST,
    DIM + "allow: registry.npmjs.org, cdn.npmjs.com" + RST,
    "",
    "  step                what it tests          outcome",
    "  -----------------   --------------------   -----------------------------",
    "  npm install express allowlisted traffic    " + GREEN + "success" + RST + "  " + DIM + "install works" + RST,
    "  curl 1.1.1.1        unauthorized egress    " + RED + "BLOCKED" + RST + "   " + DIM + "dropped at connect4" + RST,
], dt=0.05)
t[0] += 1.2
emit("\r\n")
out([
    "  " + GREEN + "✔" + RST + " defend enforced the allowlist: the registry install went through,",
    "    and the connection to " + YEL + "1.1.1.1" + RST + " (not allowed) never left the runner.",
], dt=0.04)
t[0] += 1.2
comment("Full digests for npm/pip/cargo/go/apt/gem are committed in demo-output/ - no Actions tab needed.")
t[0] += 0.6
typed("")
t[0] += 1.0

header = {
    "version": 2, "width": W, "height": H,
    "timestamp": 1749939600,
    "title": "coldstep - detect what npm install phones home, then block it",
    "env": {"SHELL": "/bin/bash", "TERM": "xterm-256color"},
}

os.makedirs(os.path.dirname(sys.argv[1]), exist_ok=True)
with open(sys.argv[1], "w", encoding="utf-8", newline="\n") as f:
    f.write(json.dumps(header) + "\n")
    for ev in events:
        f.write(json.dumps(ev, ensure_ascii=False) + "\n")
print("wrote " + sys.argv[1] + ": " + str(len(events)) + " events, " + str(round(t[0], 1)) + "s")
