#!/usr/bin/env python3
"""One Line of Earned Pride.

Writes a single original line of text to /output/entry.txt:
a quiet, earned moment of pride for someone in a scene.
"""

import os

LINE = (
    "After three summers of dawn rows beside her father, "
    "the fisherman's daughter steered the boat home alone "
    "through the chop, and he only untied the rope, "
    "stepped back, and let her go."
)


def main() -> None:
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as handle:
        handle.write(LINE + "\n")


if __name__ == "__main__":
    main()
