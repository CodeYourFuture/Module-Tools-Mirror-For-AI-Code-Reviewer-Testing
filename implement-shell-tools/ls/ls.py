import argparse
import os
import stat
import sys


def parse_args():
    parser = argparse.ArgumentParser(
        description="List directory contents",
    )
    parser.add_argument(
        "paths",
        nargs="*",
        help="The file path to process (defaults to current directory)",
    )
    parser.add_argument(
        "-a",
        action="store_true",
        dest="include_hidden",
        help="Include directory entries whose names begin with a dot ('.').",
    )
    parser.add_argument(
        "-1",
        action="store_true",
        dest="one_per_line",
        help="Force output to be one entry per line.",
    )
    return parser.parse_args()


def filter_hidden(files: list[str]) -> list[str]:
    return [name for name in files if not name.startswith(".")]


def get_visible_entries(files: list[str], include_hidden: bool):
    return files if include_hidden else filter_hidden(files)


def format_entries(files: list[str], one_per_line: bool):
    if len(files) == 0:
        return
    print(("\n" if one_per_line else "\t").join(files))


def main():
    args = parse_args()

    try:
        file_paths = args.paths if args.paths else ["."]
        include_hidden = bool(args.include_hidden)
        one_per_line = bool(args.one_per_line)

        result_files: list[str] = []
        result_dirs: dict[str, list[str]] = {}

        for file_path in file_paths:
            st = os.stat(file_path)
            # Is a file?
            if stat.S_ISREG(st.st_mode):
                result_files.append(file_path)
            # Is a directory?
            if stat.S_ISDIR(st.st_mode):
                result_dirs[file_path] = os.listdir(file_path)

        result_files = get_visible_entries(result_files, include_hidden)

        if len(file_paths) == 1:
            entries = list(result_files)
            for contents in result_dirs.values():
                filtered = get_visible_entries(contents, include_hidden)
                entries.extend(filtered)
            format_entries(entries, one_per_line)
        else:
            format_entries(result_files, one_per_line)

            for directory, contents in result_dirs.items():
                print("\n" + directory + ":")
                filtered = get_visible_entries(contents, include_hidden)
                format_entries(filtered, one_per_line)
    except OSError as err:
        print(str(err), file=sys.stderr)

    return 0


main()
