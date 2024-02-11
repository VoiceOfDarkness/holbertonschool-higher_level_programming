#!/usr/bin/python3
"""Docs for holberton checker"""


def add_attribute(obj, name: str, val: str):
    """Docs for holberton checker"""

    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    return setattr(obj, name, val)
