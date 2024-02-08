#!/usr/bin/python3
"""Docs for holberton checker"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Docs for holberton checkelir"""

    def __init__(self, size) -> None:
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size 
