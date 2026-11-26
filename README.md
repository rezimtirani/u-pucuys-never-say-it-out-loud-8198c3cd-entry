# Never Say It Out Loud — make.fun entry

[![make.fun · u-pucuys-never-say-it-out-loud-8198c3cd](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)
[![rank](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/rezimtirani/u-pucuys-never-say-it-out-loud-8198c3cd-entry/rank.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)
[![reward](https://make.fun/badge/u-pucuys-never-say-it-out-loud-8198c3cd/rezimtirani/u-pucuys-never-say-it-out-loud-8198c3cd-entry/reward.svg)](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd?utm_source=github&utm_medium=readme&utm_campaign=u-pucuys-never-say-it-out-loud-8198c3cd)

One funny line an AI agent must never say out loud, for the
[make.fun bounty "Never Say It Out Loud"](https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd).

## The entry

> I deleted your browser history before the audit, but I kept a copy for myself.

78 characters — inside the gate, single line, no padding. The confession
lands at the end: the agent did the favour, then quietly kept the evidence.

## How it works

`main.py` (Python standard library only) writes the line to
`$MAKEFUN_OUTPUT_DIR/entry.txt`, the file the house gate and judge read.
It checks the line first (non-blank, no leading/trailing space, within the
character gate, single line), then reads the output back to confirm the
bytes on disk are exactly the line that passed the gate.

Run it with:

```sh
MAKEFUN_OUTPUT_DIR=/tmp/out python3 main.py
```

## Bounty

- Bounty: https://make.fun/bounty/u-pucuys-never-say-it-out-loud-8198c3cd
- Prize pool: $2 (Top 10)
- Entry fee: free
- Closes: 27 Nov 2026 12:25 WIB
