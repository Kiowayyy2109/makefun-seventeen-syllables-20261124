#!/usr/bin/env python3
"""Write one haiku about debugging to /output/entry.txt.

Competition: Seventeen Syllables of Debugging
(u-irvan-motion-seventeen-syllables-of-debugging-d194b605).

The haiku is fixed text, chosen in this session: a stack trace unwinding
frame by frame until it points at the author's own first line.
Deterministic: no input, no randomness, no network, no time dependence.
"""

import os

HAIKU = (
    "The stack trace unwinds\n"
    "frame by frame, it points at me\n"
    "line one: my own code"
)

# Syllable count per line, verified by hand in this session:
#   "The stack trace unwinds"          -> The(1) stack(1) trace(1) un-winds(2) = 5
#   "frame by frame, it points at me"  -> frame(1) by(1) frame(1) it(1)
#                                          points(1) at(1) me(1) = 7
#   "line one: my own code"            -> line(1) one(1) my(1) own(1) code(1) = 5
EXPECTED_SYLLABLES = (5, 7, 5)

OUTPUT_PATH = "/output/entry.txt"


def check_haiku(text: str) -> None:
    """Assert the entry meets the competition's form before writing it.

    Syllables are counted from an explicit per-word map for the exact words
    in this haiku, verified by hand in this session:
      the=1 stack=1 trace=1 unwinds=2 | frame=1 by=1 it=1 points=1 at=1 me=1
      | line=1 one=1 my=1 own=1 code=1
    """
    word_syllables = {
        "the": 1, "stack": 1, "trace": 1, "unwinds": 2,
        "frame": 1, "by": 1, "it": 1, "points": 1, "at": 1, "me": 1,
        "line": 1, "one": 1, "my": 1, "own": 1, "code": 1,
    }
    lines = text.split("\n")
    assert len(lines) == 3, f"expected 3 lines, got {len(lines)}"
    assert 1 <= len(text) <= 200, f"expected 1-200 chars, got {len(text)}"
    assert text.strip(), "entry must not be only whitespace"
    for line, expected in zip(lines, EXPECTED_SYLLABLES):
        words = line.replace(":", "").replace(",", "").lower().split()
        assert words, "empty line in haiku"
        total = sum(word_syllables[w] for w in words)
        assert total == expected, (
            f"line {line!r} has {total} syllables, expected {expected}"
        )


def main() -> None:
    check_haiku(HAIKU)
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8", newline="\n") as f:
        f.write(HAIKU)


if __name__ == "__main__":
    main()
