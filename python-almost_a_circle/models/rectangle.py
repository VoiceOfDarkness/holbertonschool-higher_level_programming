#!/usr/bin/python3
"""Docs for holberton checker"""
from models.base import Base


class Rectangle(Base):
    """Docs for holberton checker"""

    def __init__(self, width: int, height, x=0, y=0, id=None) -> None:
        self.width = width
        self.height = height
        self.x = x
        self.y = y
        super().__init__(id)

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        if not isinstance(value, int):
            raise TypeError("x must be an integer")
        if value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        if not isinstance(value, int):
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """Docs for holberton checker"""

        return (self.__height * self.__width)

    def display(self):
        """Docs for holberton checker"""

        abscissa = " " * self.__x + "#" * self.__width + '\n'
        ordinate = '\n' * self.__y + abscissa * self.__height
        print(ordinate, end="")
