#!/usr/bin/python3
"""Docs for holberton checker"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """Docs for holberton checker"""

    def __init__(self, size, x=0, y=0, id=None) -> None:
        super().__init__(size, size, x, y, id)

    @property
    def size(self):
        return self.width

    @size.setter
    def size(self, value):
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Docs for holberton checker"""

        attribues = ['id', 'size', 'x', 'y']
        if args and len(args) != 0:
            for key, val in zip(attribues, args):
                setattr(self, key, val)
        elif kwargs and len(kwargs) != 0:
            for key, val in kwargs.items():
                if key in attribues:
                    setattr(self, key, val)

    def to_dictionary(self):
        """Docs for holberton checker"""

        return {
            "id": self.id,
            "x": self.x,
            "size": self.size,
            "y": self.y
        }

    def __str__(self):
        return ("[Square] ({}) {}/{} - {}"
                .format(self.id, self.x, self.y, self.width))
