#!/usr/bin/python3
"""This module contains load_from_json_file function"""
import json


def load_from_json_file(filename):
    """load_from_json_file function"""

    with open(filename, "r") as file:
        obj = json.loads(file.read())
    return obj
