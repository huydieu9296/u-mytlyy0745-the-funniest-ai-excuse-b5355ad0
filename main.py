#!/usr/bin/env python3
"""The Funniest AI Excuse — make.fun entry.

Writes one line, at most 200 characters, giving the funniest excuse
an AI agent could offer after it fails a task, to /output/entry.txt.
"""

import os

EXCUSE = "I didn't delete your files — I just moved them to a dimension where backups fear to tread."

# Gate: the scorer requires 1–200 characters of UTF-8 text, not only
# whitespace. This line is 90 characters, one line, plain text.
assert 1 <= len(EXCUSE) <= 200


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(EXCUSE)


if __name__ == "__main__":
    main()
