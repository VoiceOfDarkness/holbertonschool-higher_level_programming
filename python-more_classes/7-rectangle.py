#!/usr/bin/python3
"""Docs for holberton checker"""


class Rectangle:
    """Docs for holberton checker"""

    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0) -> None:
        self.width = width
        self.height = height
        type(self).number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    def area(self):
        return (self.__width * self.__height)

    def perimeter(self):
        if self.width == 0 or self.height == 0:
            return 0
        return ((self.__width * 2) + (self.__height * 2))

    def __str__(self) -> str:
        result = []
        if self.__width == 0 or self.__height == 0:
            return ""
        for i in range(self.__height):
            [result.append(str(self.print_symbol)) for j in range(self.__width)]
            if i != self.__height - 1:
                result.append('\n')
        return "".join(result)

    def __repr__(self) -> str:
        result = "Rectangle(" + str(self.__width) + ", " \
                + str(self.__height) + ")"
        return result

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
