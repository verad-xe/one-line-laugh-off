#!/usr/bin/env python3
"""One-Line Laugh-Off — one funny line, written to entry.txt.

The program takes no input and needs no network. It writes exactly one
sentence (at most 200 characters) to $MAKEFUN_OUTPUT_DIR/entry.txt.
"""

import os

LINE = (
    "My smart fridge sent me a breakup text: it is tired of holding "
    "my leftovers and my unrealistic expectations about my diet."
)


def main() -> None:
    # Gate self-check: the sealed scorer requires entry.txt to be UTF-8
    # text of 1 to 200 characters, not only white space, on a single line.
    assert 1 <= len(LINE) <= 200, f"line is {len(LINE)} chars, must be 1-200"
    assert "\n" not in LINE, "line must be a single line"
    assert LINE.strip(), "line must not be only white space"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(LINE + "\n")


if __name__ == "__main__":
    main()
