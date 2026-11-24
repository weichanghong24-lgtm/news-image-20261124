#!/usr/bin/env python3
"""Entrypoint for the make.fun news-image-20261124 entry.

Standard library only. Copies the pre-rendered entry image
(entry.png, committed beside this file) to
$MAKEFUN_OUTPUT_DIR/entry.png, as the bounty requires.
"""

import os
import shutil
import sys


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    src = os.path.join(here, "entry.png")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    dst = os.path.join(out_dir, "entry.png")
    if not os.path.isfile(src):
        print(f"entry.png not found next to main.py ({src})", file=sys.stderr)
        return 1
    shutil.copyfile(src, dst)
    print(f"copied {src} -> {dst} ({os.path.getsize(dst)} bytes)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
