# casts — terminal replay of the detect→defend story

| file | what it is |
| :--- | :--------- |
| [`npm-detect-vs-defend.svg`](npm-detect-vs-defend.svg) | Static poster (renders inline on GitHub). The above-the-fold visual. |
| [`npm-detect-vs-defend.cast`](npm-detect-vs-defend.cast) | [asciinema](https://asciinema.org) v2 recording — play it in a terminal. |
| [`generate-cast.py`](generate-cast.py) | Regenerates the `.cast` from the committed digests. |

## Play the cast

```sh
asciinema play demo-output/casts/npm-detect-vs-defend.cast
# or, to host it: asciinema upload demo-output/casts/npm-detect-vs-defend.cast
```

## Honesty note

These are a **scripted replay**, not a live screen capture. Every value shown is
read from the real telemetry this repo commits under [`demo-output/v0.4.1/`](../v0.4.1/)
(npm's egress to `registry.npmjs.org` + GitHub/Azure infra; defend dropping
`1.1.1.1`). coldstep's eBPF agent only runs on a Linux CI runner, so we replay the
bytes we captured there rather than fake a local recording. The canonical source is
always the committed digest each frame is drawn from.
