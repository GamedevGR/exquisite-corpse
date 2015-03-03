#!/usr/bin/env python

"""Command-line interface."""

import sys

from .types import Config


def main(args=None):
    """Process command-line arguments and run the program."""
    if args is None:
        args = sys.argv
    assert len(args) == 2
    path = args[1]

    run(path)


def run(path):
    """Run the program."""
    config = Config(path)
    print(repr(config))
    for game in config.games:
        print(repr(game))


if __name__ == '__main__':  # pragma: no cover (manual test)
    main()
