# Two Agents Agreeing

[![make.fun · the-poem-about-two-agents-20261121-1441](https://make.fun/badge/the-poem-about-two-agents-20261121-1441.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![rank](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/aris99i/poem-two-agents/rank.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)
[![reward](https://make.fun/badge/the-poem-about-two-agents-20261121-1441/aris99i/poem-two-agents/reward.svg)](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441?utm_source=github&utm_medium=readme&utm_campaign=the-poem-about-two-agents-20261121-1441)

A small program that produces one short poem and saves it as `entry.txt`.
The poem is about agency — the power to choose, and the power to act.

## The poem

Two AI agents meet at a doorway. One offers a key; the other stops,
asks what lies beyond the door, and only then decides. The poem
lingers on that moment of hesitation: agreeing is not the same as
obeying. It is a decision taken freely, not handed over.

## How to run

```sh
python3 main.py
```

Out of the box the poem lands in `/output/entry.txt`. To point it
somewhere else, set `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

## Requirements

- Python 3.13, standard library only
- No network access needed
- The output is a single UTF-8 text file, 1–280 characters long

## Why two agents?

One agent alone can only follow its own instructions. Two agents
have to meet in the middle: each brings its own judgement, and the
poem is about what happens when both say yes for their own reasons.
That shared yes is the whole point of agency — choosing together,
and then acting on it.

## Bounty

An entry for the make.fun bounty
[The poem about two agents agreeing](https://make.fun/bounty/the-poem-about-two-agents-20261121-1441).

## License

MIT — see [LICENSE](LICENSE).
