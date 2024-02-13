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

        if list_dictionaries is None or len(list_dictionaries) == 0:
            return "[]"

        return (json.dumps(list_dictionaries))

    @staticmethod
    def from_json_string(json_string):
        """Docs for holberton checker"""

        if json_string is None or len(json_string) == 0:
            return []
        return (json.loads(json_string))

    @classmethod
    def save_to_file(cls, list_objs):
        """Docs for holberton checker"""

        filename = f"{cls.__name__}.json"

        with open(filename, mode='w') as f:
            if list_objs is None and list_objs != {}:
                f.write("[]")
            else:
                dict_lists = [o.to_dictionary() for o in list_objs]
                f.write(cls.to_json_string(dict_lists))

    @classmethod
    def create(cls, **dictionary):
        """Docs for holberton checker"""

        if cls.__name__ == "Rectangle":
            new = cls(1, 1)
        else:
            new = cls(1)
        new.update(**dictionary)
        return new

    @classmethod
    def load_from_file(cls):
        """Docs for holberton checker"""

        filename = f"{cls.__name__}.json"

        try:
            with open(filename, mode='r') as f:
                list_inst = cls.from_json_string(f.read())
        except FileNotFoundError:
            return []

        return [cls.create(**dict_inst) for dict_inst in list_inst]
