#!/usr/bin/python3
"""Docs for holberton checker"""


def append_after(filename="", search_string="", new_string=""):
    """Docs for holberton checker"""

    with open(filename, "r") as file:
        lines = file.readlines()

    new_lines = []

    for i in range(len(lines)):
        new_lines.append(lines[i])
        if search_string in lines[i]:
            new_lines.append(new_string)

    with open(filename, "w") as file:
        file.writelines(new_lines)
