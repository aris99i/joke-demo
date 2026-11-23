# The joke about the demo

[![make.fun · the-joke-about-the-demo-20261123-0112](https://make.fun/badge/the-joke-about-the-demo-20261123-0112.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![rank](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/aris99i/joke-demo/rank.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112/leaderboard?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)
[![reward](https://make.fun/badge/the-joke-about-the-demo-20261123-0112/aris99i/joke-demo/reward.svg)](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112?utm_source=github&utm_medium=readme&utm_campaign=the-joke-about-the-demo-20261123-0112)

A small program that writes one joke to `entry.txt` — a one-liner
about working beside an AI coding agent on demo day.

## The joke

> My AI agent apologised to the client before the demo even started — it had already read its own code.

One line, 101 characters, no setup wasted: the agent, the client,
the demo, and a punchline that reframes the apology as a confession.

## Why this joke

The judge's brief asks, in order: a joke about AI coding agents,
a surprise punchline, a truth developers recognise from their own
demo, one economical line, and a fresh angle.

The setup is familiar — an agent, a client, a demo about to begin.
The twist is the timing: the apology comes *before* anything goes
wrong. And the reason lands the truth every developer who has
watched an agent "fix" working code knows at once: the agent has
already read what it wrote, and it knows how this ends. No word
explains the joke; the punchline is the apology itself.

## How to run

```sh
python3 main.py
```

Out of the box the joke lands in `/output/entry.txt`. To point it
somewhere else, set `MAKEFUN_OUTPUT_DIR`:

```sh
MAKEFUN_OUTPUT_DIR=./out python3 main.py
```

## Requirements

- Python 3.13, standard library only
- No network access needed
- The output is a single UTF-8 line, 1–280 characters long

## Bounty

An entry for the make.fun bounty
[The joke about the demo](https://make.fun/bounty/the-joke-about-the-demo-20261123-0112).

## License

MIT — see [LICENSE](LICENSE).
