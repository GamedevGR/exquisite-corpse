#!/usr/bin/env python3

if __name__ == '__main__':

    import sys

    sys.stderr.write("args: {}\n".format(", ".join(a for a in sys.argv)))

    print("{'good-big': 123, 'bad-big': 456}")
