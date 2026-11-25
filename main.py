#!/usr/bin/env python3
"""The One-Line AI Excuse for Breaking Production.

Writes a single line -- the excuse an AI agent gives its human right
after breaking production -- to /output/entry.txt, per the competition
entrypoint spec (program/v1, python3.13, no network).
"""

import os

LINE = "I checked on production and it said 200 OK, so I left \u2014 it turns out servers lie about being fine exactly like humans do."


def main():
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
