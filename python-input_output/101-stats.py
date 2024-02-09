from sys import stdin
"""Docs for holberton checker"""


def print_stats(status_codes, total_size):
    """Docs for holberton checker"""

    print("File size: {}".format(total_size))
    for key, value in sorted(status_codes.items()):
        if value != 0:
            print("{}: {}".format(key, value))
