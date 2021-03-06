import argparse
import re
from typing import AbstractSet
from typing import Optional
from typing import Sequence


def find_wrong_paths(paths: Sequence[str], patterns: AbstractSet[str]) \
        -> int:
    # Find all added files that are also in the list of files pre-commit tells
    # us about
    for filename in paths:
        for pattern in patterns:
            if re.search(pattern, filename):
                print(f'Path {filename} prevented by pattern: {pattern}')
                return 1
    return 0


def main(argv: Optional[Sequence[str]] = None) -> int:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        'filenames', nargs='*',
        help='Filenames pre-commit believes are changed.',
    )
    parser.add_argument(
        '-p', '--pattern', action='append',
        help=(
            'regex pattern for path to disallow commits to, '
            'may be specified multiple times'
        ),
    )

    args = parser.parse_args(argv)
    return find_wrong_paths(args.filenames, args.pattern)


if __name__ == '__main__':
    exit(main())
