#!/usr/bin/python3
"""Docs for holberton checker"""


def read_file(filename=""):
    """Docs for holberton checker"""

    with open(filename, 'r', encoding='utf-8') as e:
        print(e.read(), end='')
