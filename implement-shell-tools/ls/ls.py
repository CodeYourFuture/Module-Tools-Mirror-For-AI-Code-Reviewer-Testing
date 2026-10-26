"""List directory entries, one per line."""

import argparse
from pathlib import Path
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-1", action="store_true", help="print one entry per line")
    parser.add_argument("-a", "--all", action="store_true", help="include hidden entries")
    parser.add_argument("directory", nargs="?", default=".")
    args = parser.parse_args()

    try:
        entries = sorted(Path(args.directory).iterdir(), key=lambda entry: entry.name)
        for entry in entries:
            if args.all or not entry.name.startswith("."):
                print(entry.name)
    except OSError as error:
        print(f"ls: {error}", file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    sys.exit(main())
