#!/usr/bin/python3
"""This module contains save_to_json_file function"""
import json


def save_to_json_file(my_obj, filename):
    """save_to_json_file function"""

    with open(filename, "w") as file:
        json_string = json.dumps(my_obj)
        file.write(json_string)
