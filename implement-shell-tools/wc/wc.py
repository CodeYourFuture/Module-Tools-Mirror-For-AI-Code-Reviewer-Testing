"""Count lines, words, and bytes in files."""

import argparse
from pathlib import Path
import sys


def count_file(filename):
    text = Path(filename).read_bytes().decode("utf-8")
    return len(text.splitlines()), len(text.split()), len(text)


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("-l", action="store_true", help="print line counts")
    parser.add_argument("-w", action="store_true", help="print word counts")
    parser.add_argument("-c", action="store_true", help="print byte counts")
    parser.add_argument("files", nargs="+")
    args = parser.parse_args()
    selected = [args.l, args.w, args.c]
    if not any(selected):
        selected = [True, True, True]

    def print_counts(counts, label):
        values = [str(value) for value, enabled in zip(counts, selected) if enabled]
        print(" ".join([*values, label]))

    totals = [0, 0, 0]
    successful = 0
    status = 0
    for filename in args.files:
        try:
            counts = count_file(filename)
        except (OSError, UnicodeError) as error:
            print(f"wc: {filename}: {error}", file=sys.stderr)
            status = 1
            continue
        print_counts(counts, filename)
        totals = [total + value for total, value in zip(totals, counts)]
        successful += 1
    if successful > 1:
        print_counts(totals, "total")
    return status


if __name__ == "__main__":
    sys.exit(main())
