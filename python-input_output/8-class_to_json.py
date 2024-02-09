#!/usr/bin/python3
"""This module contains class_to_json function"""


def class_to_json(obj: object):
    """class_to_json function"""

    return obj.__dict__
