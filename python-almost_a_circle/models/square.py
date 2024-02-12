#!/usr/bin/python3
"""Docs for holberton checker"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Docs for holberton checker"""

    def __init__(self, size, x=0, y=0, id=None) -> None:
        super().__init__(size, size, x, y, id)

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))
