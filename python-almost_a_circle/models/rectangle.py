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
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.__x = x

    @property
    def y(self)
        return self.__y

    @y.setter
    def y(self, value):
        self.__y = value

