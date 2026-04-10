import argparse
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="Reads file(s) and writes them to the standard output",
    )
    parser.add_argument("paths", nargs="+", help="The file path(s) to process")
    parser.add_argument(
        "-n",
        action="store_true",
        dest="number_all",
        help="Number the output lines, starting at 1.",
    )
    parser.add_argument(
        "-b",
        action="store_true",
        dest="number_nonblank",
        help="Number only non-blank output lines, starting at 1.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    try:
        for path in args.paths:
            line_num = 1

            with open(path, "r", encoding="utf-8") as file:
                for raw_line in file:
                    line = raw_line.rstrip("\n")
                    is_blank = line.strip() == ""
                    should_number = args.number_all or (
                        args.number_nonblank and not is_blank)

                    if should_number:
                        print(f"{line_num}  {line}")
                        line_num += 1
                    else:
                        print(line)
    except OSError as err:
        print(err, file=sys.stderr)

    return 0


main()
