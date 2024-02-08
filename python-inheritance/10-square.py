#!/usr/bin/python3
"""Docs for holberton checker"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Docs for holberton checker"""

    def __init__(self, size) -> None:
        self.integer_validator("size", size)
        self.__size = size

    def __str__(self) -> str:
        return f"[Rectangle] {self.__size}/{self.__size}"

    def area(self):
        return (self.__size * 2)
