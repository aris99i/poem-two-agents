# Two Agents Agreeing

[![make.fun bounty](https://img.shields.io/badge/make.fun-bounty-blue)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441)
[![Python 3.13](https://img.shields.io/badge/python-3.13-blue)](https://www.python.org/downloads/release/python-3130/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

A tiny program that writes one short poem about agency — the power
to choose and to act — to `entry.txt`.

## The poem

Two AI agents stand at a threshold. One holds out a key; the other
pauses, asks what the door is for, and only then chooses. The poem
is about that pause: agreement is not obedience, it is a choice
made, not given.

## Run it

```sh
python3 main.py
```

By default the poem is written to `/output/entry.txt`. Set
`MAKEFUN_OUTPUT_DIR` to choose another directory:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

## Requirements

- Python 3.13 (standard library only)
- No network access
- Output is a single UTF-8 text file, 1–280 characters

## Entry

Built for the make.fun bounty
[The poem about two agents agreeing](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441).

## License

MIT — see [LICENSE](LICENSE).
