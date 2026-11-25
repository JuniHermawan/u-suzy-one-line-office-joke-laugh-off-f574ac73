#!/usr/bin/env python3
"""One-Line Office Joke Laugh-Off entry.

Writes a single original one-line office joke to $MAKEFUN_OUTPUT_DIR/entry.txt
(default /output). Deterministic, stdlib only, no network, no randomness,
no clock. The joke text is a fixed string.

Revision (reviser session): the punchline now lands a second sting -- the
candle is not just an absurd remedy for burnout, it is the boss's cheap
substitute for a raise. The program also self-checks the competition gate
(UTF-8, 1-200 characters, one line, not only whitespace) before writing,
so a future wording slip fails loudly instead of shipping an invalid entry.
"""

import os

JOKE = "I told my boss I was burned out and he gave me a candle, cheaper than a raise."


def _check_gate(text: str) -> None:
    """Fail loudly if the joke would not pass the competition gate."""
    text.encode("utf-8")  # must be valid UTF-8
    if not 1 <= len(text) <= 200:
        raise ValueError(f"joke is {len(text)} characters, gate needs 1-200")
    if "\n" in text or "\r" in text:
        raise ValueError("joke must be a single line")
    if not text.strip():
        raise ValueError("joke must not be only whitespace")


def main() -> None:
    _check_gate(JOKE)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="") as f:
        f.write(JOKE)


if __name__ == "__main__":
    main()
