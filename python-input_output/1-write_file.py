#!/usr/bin/python3
"""Docs for holberton checker"""


def write_file(filename="", text=""):
    """Docs for holberton checker"""

    with open(filename, mode='a+', encoding='utf-8') as f:
        result = f.write(text)
    return result
