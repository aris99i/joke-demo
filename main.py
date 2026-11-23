#!/usr/bin/env python3
"""The joke about the demo.

Writes one joke about working beside an AI coding agent to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output/entry.txt).

Python 3.13, standard library only, no network access, deterministic:
the same bytes are written on every run.
"""

import os

JOKE = (
    "My AI agent apologised to the client before the demo even started "
    "\u2014 it had already read its own code.\n"
)


def main() -> None:
    # One line, 1-280 code points, not only white space: the gate
    # the bounty requires, checked here before anything is written.
    if not 1 <= len(JOKE) <= 280:
        raise ValueError("joke must be 1-280 code points")
    if "\n" in JOKE.strip():
        raise ValueError("joke must be a single line")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(JOKE)


if __name__ == "__main__":
    main()
