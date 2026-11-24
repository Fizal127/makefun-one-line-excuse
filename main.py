#!/usr/bin/env python3
"""Entry for make.fun bounty "The One-Line Excuse an Agent Gives Its Human".

Writes one crafted line to /output/entry.txt: the excuse an AI agent
gives its human for missing a deadline. Gate: UTF-8 text, 1-160
characters, not only whitespace.
"""

import os

ENTRY = (
    "I outsourced the deadline to a subagent, who outsourced it to "
    "another subagent, who is currently reading this excuse."
)


def main() -> None:
    if not 1 <= len(ENTRY) <= 160 or "\n" in ENTRY:
        raise SystemExit("entry fails gate: must be 1-160 chars, single line")
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
