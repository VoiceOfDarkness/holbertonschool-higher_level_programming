#!/usr/bin/python3
"""This module contains a class BaseGeometry"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(BaseGeometry):
    """class Rectangl, abstract class"""

    def __init__(self, width, height) -> None:
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
