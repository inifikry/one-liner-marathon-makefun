#!/usr/bin/env python3
"""One-Liner Marathon entry.

Writes a single original one-line joke to /output/entry.txt.
Deterministic: no network, no randomness, no files outside this repo.
"""

import os

JOKE = "My smartwatch congratulated me for standing up, which is the saddest applause I've ever received."


def main() -> None:
    # Guard the gate: entry must be 1-280 chars, not only whitespace.
    assert 1 <= len(JOKE) <= 280 and JOKE.strip(), "joke fails the gate"
    assert "\n" not in JOKE, "must be a single line"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
