#!/usr/bin/python3
"""Docs for holberton checker"""
import json


class Base:
    """Docs for holberton checker"""

    __np_objects = 0

    def __init__(self, id=None) -> None:
        if id is not None:
            self.id = id
        else:
            Base.__np_objects += 1
            self.id = Base.__np_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Docs for holberton checker"""

        if not list_dictionaries and len(list_dictionaries) != 0:
            return "[]"

        return (json.dumps(list_dictionaries))
