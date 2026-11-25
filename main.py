#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Deterministic, stdlib only, no network, no randomness,
no clock. The joke text is a fixed string.
"""

import os

JOKE = "I told my boss I was burned out and he gave me a candle."


def main() -> None:
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
