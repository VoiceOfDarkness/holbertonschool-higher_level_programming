#!/usr/bin/python3
"""Docs for holberton checker"""


class Base:
    """Docs for holberton checker"""

    __np_objects = 0

    def __init__(self, id=None) -> None:
        if id is not None:
            self.id = id
        else:
            Base.__np_objects += 1
            self.id = Base.__np_objects 
