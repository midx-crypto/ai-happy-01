#!/usr/bin/env python3
"""Copy the vendored happy image to /output/entry.png, byte for byte.

The image lives in this repository as entry.png: a capybara soaking in a
steaming hot spring at sunrise, a tiny orange kitten in a knitted coral
scarf riding on its back, and a duckling perched on its head, cherry
blossom petals drifting through warm golden light. This program only
copies it, so both runs write identical bytes and no network is needed.
"""

import os
import shutil

SRC = os.path.join(os.path.dirname(os.path.abspath(__file__)), "entry.png")
DST = os.path.join(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"), "entry.png")


def main() -> None:
    os.makedirs(os.path.dirname(DST), exist_ok=True)
    shutil.copyfile(SRC, DST)


if __name__ == "__main__":
    main()
