#!/usr/bin/env python3
"""news-image-20261118: ship the bundled collage as the entry image.

The repository holds the finished 1024x1024 collage as image.jpg
(summing up the world news of Wednesday 18 November 2026). This
program's only job is to deliver those exact bytes to entry.png in
the output directory. The competition names the file entry.png
whether the bytes are PNG or JPEG, and requires at most 1 MiB and
at most 1024x1024 pixels; the copy is byte-for-byte, so every run
produces identical output.
"""
import os
import shutil


def main():
    here = os.path.dirname(os.path.abspath(__file__))
    source = os.path.join(here, "image.jpg")
    if not os.path.isfile(source):
        raise SystemExit("missing bundled image: " + source)
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    target = os.path.join(out_dir, "entry.png")
    shutil.copyfile(source, target)


if __name__ == "__main__":
    main()
