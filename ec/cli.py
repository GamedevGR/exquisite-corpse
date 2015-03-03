#!/usr/bin/env python

"""Command-line interface."""

import sys


def main(args=None):
    """Process command-line arguments and run the program."""
    if args is None:
        args = sys.argv
    assert len(args) == 2
    path = args[1]

    run(path)


def run(path):
    """Run the program."""
    print(path)


if __name__ == '__main__':  # pragma: no cover (manual test)
    main()
