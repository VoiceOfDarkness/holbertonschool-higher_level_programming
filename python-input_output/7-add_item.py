#!/usr/bin/python3
"""This module contains script that add all arguments"""
from sys import argv

save_to_json_file = __import__("5-save_to_json_file").save_to_json_file
load_from_json_file = __import__("6-load_from_json_file").load_from_json_file


def main():
    """main function of programm"""

    try:
        obj = load_from_json_file("add_item.json")
    except FileNotFoundError:
        obj = []
    obj += argv[1:]
    save_to_json_file(obj, "add_item.json")


if __name__ == "__main__":
    main()
