#!/usr/bin/python3
"""Docs for holberton checker"""


class LockedCLass:
    """
    Prevent the user from instantiating new LockedClass attributes
    for anything but attributes called 'first_name'.
    """

    __slots__ = ["first_name"]
