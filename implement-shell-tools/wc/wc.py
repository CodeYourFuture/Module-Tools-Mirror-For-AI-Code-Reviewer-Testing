import argparse
import os
import sys

from tabulate import tabulate


def parse_args():
    parser = argparse.ArgumentParser(
        description="word, line and byte count",
    )
    parser.add_argument("paths", nargs="+",
                        help="The file path(s) to process.")
    parser.add_argument(
        "-l",
        "--lines",
        action="store_true",
        help="The number of lines in each input file is written to the standard output.",
    )
    parser.add_argument(
        "-w",
        "--words",
        action="store_true",
        help="The number of words in each input file is written to the standard output.",
    )
    parser.add_argument(
        "-c",
        "--bytes",
        action="store_true",
        dest="bytes",
        help="The number of bytes in each input file is written to the standard output.",
    )
    return parser.parse_args()


def main():
    args = parse_args()

    try:
        file_paths: list[str] = args.paths
        results: dict[str, dict[str, int]] = {}

        for file_path in file_paths:
            stats = os.stat(file_path)
            count = {"lines": 0, "words": 0, "bytes": stats.st_size}

            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    count["lines"] += 1
                    trimmed = line.strip()
                    if len(trimmed) > 0:
                        count["words"] += len(trimmed.split())

            results[file_path] = count

        if len(file_paths) > 1:
            total = {"lines": 0, "words": 0, "bytes": 0}
            for file_count in results.values():
                total["lines"] += file_count["lines"]
                total["words"] += file_count["words"]
                total["bytes"] += file_count["bytes"]
            results["total"] = total

        no_options_provided = not (args.lines or args.words or args.bytes)
        selected_option_keys: list[str] = []

        if args.lines:
            selected_option_keys.append("lines")
        if args.words:
            selected_option_keys.append("words")
        if args.bytes:
            selected_option_keys.append("bytes")

        output_columns = [
            "lines", "words", "bytes"] if no_options_provided else selected_option_keys
        rows: list[list[str | int]] = []
        for name, values in results.items():
            rows.append([name] + [values[column] for column in output_columns])

        if no_options_provided:
            print(tabulate(rows, headers=[
                  "index"] + output_columns))
        else:
            print(tabulate(rows, headers=[
                  "index"] + output_columns))
    except OSError as err:
        print(str(err), file=sys.stderr)

    return 0


main()
