#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single line -- the excuse an AI agent gives its human right
after breaking production -- to /output/entry.txt, per the competition
entrypoint spec (program/v1, python3.13, no network).

The line is assembled from two parts so the setup and the punchline
stay readable on their own; the assembled text is exactly the entry
line, one line, no trailing newline.
"""

import os

_SETUP = "I checked on production and it said 200 OK, so I left"
_PUNCHLINE = "it turns out servers lie about being fine exactly like humans do."


def build_line(setup=_SETUP, punchline=_PUNCHLINE):
    """Join the setup and the punchline with an em dash."""
    return f"{setup} \u2014 {punchline}"


LINE = build_line()


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
