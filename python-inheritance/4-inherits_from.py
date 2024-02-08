#!/usr/bin/python3
"""Docs for holberton checker"""


def inherits_from(obj, a_class):
    """Docs for holberton checker"""

    return type(obj) is not a_class and issubclass(type(obj), a_class)
