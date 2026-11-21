#!/usr/bin/env python3
"""Two Agents Agreeing.

Writes a single short poem about agency -- the power to choose
and to act -- to $MAKEFUN_OUTPUT_DIR/entry.txt.

Python 3.13, standard library only, no network access, deterministic:
the same bytes are written on every run.
"""

import os

POEM = (
    "One agent held the key out, flat on its palm.\n"
    "The other did not take it. It asked what the door was for.\n"
    "Silence. Then a nod -- a choice, made, not given.\n"
    "The lock turned from the inside.\n"
    "Two minds. One door. Open.\n"
)


def main() -> None:
    if not 1 <= len(POEM) <= 280:
        raise ValueError("poem must be 1-280 code points")
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as handle:
        handle.write(POEM)


if __name__ == "__main__":
    main()
