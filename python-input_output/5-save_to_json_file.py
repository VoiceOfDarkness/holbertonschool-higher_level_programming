#!/usr/bin/python3
"""Docs for holberton checker"""
import json


def save_to_json_file(my_obj, filename):
    """Docs for holberton checker"""

    with open(filename, 'w') as f:
        f.write(json.dumps(filename))
