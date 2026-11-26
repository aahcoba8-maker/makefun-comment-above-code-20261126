#!/usr/bin/env python3
"""The Comment Above the Code - entrypoint.

Reads the one-line comment from entry.txt next to this script, prints it,
and writes it to $MAKEFUN_OUTPUT_DIR/entry.txt when the grader sets that
variable (the grader mounts the repo read-only, so the deliverable must go
to the output directory, never next to the script).
"""

import os
import sys


def main() -> int:
    here = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(here, "entry.txt"), encoding="utf-8") as f:
        text = f.read()
    sys.stdout.write(text)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR")
    if out_dir:
        os.makedirs(out_dir, exist_ok=True)
        with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
            f.write(text)
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
