#!/usr/bin/env python3
"""Write the entry image for make.fun's news-image-20261118 competition.

The repository ships the finished collage as ``image.jpg`` beside this
program: a 1024x1024 JPEG summing up the world news of Wednesday
18 November 2026. The program's whole job is to deliver those exact
bytes to ``entry.png`` in the output directory -- the competition
accepts a PNG or a JPEG (told apart by the file's first bytes) while
keeping the name ``entry.png`` either way, at most 1 MiB and at most
1024x1024 pixels.

At trial time the repository is mounted read-only and the working
directory is not guaranteed, so the source is resolved relative to
this file's own location. The copy is streamed in fixed-size chunks,
which keeps memory bounded and the output byte for byte identical to
the source on every run.
"""

import os
import sys
from pathlib import Path

SOURCE_NAME = "image.jpg"
OUTPUT_NAME = "entry.png"
CHUNK_SIZE = 64 * 1024


def source_path() -> Path:
    """The bundled image, resolved next to this program file."""
    return Path(__file__).resolve().parent / SOURCE_NAME


def output_path() -> Path:
    """$MAKEFUN_OUTPUT_DIR if set, else /output, as a Path."""
    directory = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    return Path(directory) / OUTPUT_NAME


def copy_image(source: Path, destination: Path) -> None:
    destination.parent.mkdir(parents=True, exist_ok=True)
    with source.open("rb") as reader, destination.open("wb") as writer:
        while chunk := reader.read(CHUNK_SIZE):
            writer.write(chunk)


def main() -> int:
    copy_image(source_path(), output_path())
    return 0


if __name__ == "__main__":
    sys.exit(main())
