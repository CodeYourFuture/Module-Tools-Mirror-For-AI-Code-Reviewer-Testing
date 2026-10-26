"""Concatenate files, optionally numbering their lines."""

import argparse
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-n", action="store_true", help="number every line")
    parser.add_argument("-b", action="store_true", help="number nonempty lines")
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()
    status = 0

    for filename in args.files:
        line_number = 1
        try:
            with Path(filename).open(encoding="utf-8", newline="") as source:
                for line in source:
                    number_line = args.n or (args.b and bool(line.strip()))
                    if number_line:
                        sys.stdout.write(f"{line_number:6}\t")
                        line_number += 1
                    sys.stdout.write(line)
        except (OSError, UnicodeError) as error:
            print(f"cat: {filename}: {error}", file=sys.stderr)
            status = 1

    return status


if __name__ == "__main__":
    sys.exit(main())
