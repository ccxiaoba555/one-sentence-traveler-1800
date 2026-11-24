#!/usr/bin/env python3
"""One sentence for a traveler from 1800.

Writes a single sentence explaining the modern internet to someone
arriving from the year 1800 to /output/entry.txt, as the make.fun
"One Sentence for a Traveler from 1800" bounty requires.

The sentence is built only from things a person from 1800 already
knows -- a road, a house, a letter, a book, a pen, ink -- and holds
one picture: a road of light joining every house on earth, so a
letter you write crosses the world and any book you ask for arrives
before the ink on your pen is dry. No word in it was coined after
the traveler's time, and it names no feature list, only that road.
"""

import os
import re

OUT_PATH = "/output/entry.txt"

SENTENCE = (
    "Imagine a road of light joining every house on earth, so a letter "
    "you write reaches the far side of the world, and any book you ask "
    "for arrives, before the ink on your pen is dry."
)

# Words coined after 1800 that must never appear in the sentence.
FORBIDDEN = {
    "internet", "computer", "website", "email", "online", "digital",
    "screen", "phone", "telephone", "television", "radio", "video",
    "software", "network", "server", "browser", "download", "upload",
    "wifi", "pixel", "app", "blog", "chat", "click", "link", "web",
}


def validate(text: str) -> None:
    """Check the entry against the bounty's gate before writing it."""
    if not 1 <= len(text) <= 200:
        raise SystemExit(
            f"sentence is {len(text)} characters, must be 1-200"
        )
    if text.strip() != text or not text:
        raise SystemExit("entry must not be only white space")
    if text.count(".") != 1 or not text.endswith("."):
        raise SystemExit("entry must be exactly one sentence")
    words = {w.lower() for w in re.findall(r"[A-Za-z]+", text)}
    bad = sorted(words & FORBIDDEN)
    if bad:
        raise SystemExit(f"words coined after 1800: {', '.join(bad)}")


def main() -> None:
    text = SENTENCE.strip()
    validate(text)
    os.makedirs(os.path.dirname(OUT_PATH), exist_ok=True)
    with open(OUT_PATH, "w", encoding="utf-8") as f:
        f.write(text)
    print(f"wrote {len(text)} characters to {OUT_PATH}")
    print(text)


if __name__ == "__main__":
    main()
