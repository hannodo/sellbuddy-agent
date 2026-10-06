#!/usr/bin/env python3
"""Build a shareable ZIP using only the explicit public manifest."""
import argparse
import zipfile
from pathlib import Path
from install import ROOT, public_files


def build(output, root=ROOT):
    members = list(public_files(root))
    output = Path(output).absolute()
    if any(p.is_symlink() for p in [output, *output.parents]):
        raise ValueError("Output path must not contain symlinks")
    # Exclusive creation: never overwrite an existing archive.
    with output.open("xb") as stream:
        with zipfile.ZipFile(stream, "w", zipfile.ZIP_DEFLATED) as archive:
            for member in members:
                archive.write(root / member, "sellbuddy-agent/" + member.as_posix())
    return output


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--output", required=True)
    args = parser.parse_args()
    try:
        print("Created:", build(args.output))
    except (ValueError, OSError) as error:
        parser.exit(1, str(error) + "\n")


if __name__ == "__main__":
    main()
