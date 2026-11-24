#!/usr/bin/env python3
"""One Line, One Minute: The Funniest AI Excuse.

Writes a single one-line excuse — the funniest excuse an AI agent gives
its human for a missed deadline — to /output/entry.txt, exactly as the
competition gate requires: UTF-8 text, 1 to 200 characters, one line.

The excuse is 138 characters. It is written with no trailing newline, so
the file holds exactly 138 bytes and the gate counts exactly the line.
"""

import os

EXCUSE = (
    "I was on time, but I hallucinated a second deadline, panicked, "
    "and spent the whole day apologizing to a calendar event that doesn't exist."
)


def main() -> None:
    line = EXCUSE.strip()
    assert "\n" not in line, "the excuse must be exactly one line"
    assert 1 <= len(line) <= 200, f"excuse is {len(line)} chars, must be 1-200"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8", newline="") as f:
        f.write(line)
    print(line)


if __name__ == "__main__":
    main()
