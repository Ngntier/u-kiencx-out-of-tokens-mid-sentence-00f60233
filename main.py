"""Out of Tokens, Mid-Sentence — make.fun one-liner bounty entry.

Writes a single funny error message (one line, at most 140 characters) to
$MAKEFUN_OUTPUT_DIR/entry.txt (default /output). The joke is performative:
the error message itself runs out of tokens mid-word.
"""

import os

ENTRY = (
    "Error: out of tokens. I was about to say something brilliant, "
    "but the meter ran out mid-"
)


def main() -> None:
    output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(output_dir, exist_ok=True)
    path = os.path.join(output_dir, "entry.txt")
    with open(path, "w", encoding="utf-8") as f:
        f.write(ENTRY + "\n")


if __name__ == "__main__":
    main()
