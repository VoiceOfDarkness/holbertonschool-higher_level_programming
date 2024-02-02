#!/usr/bin/python3
"""function that prints a text with 2 new lines after each of /
these characters: ., ? and :"""


def text_indentation(text):
    """
    function that prints a text with 2 new lines after each /
    of these characters: ., ? and :
    unit tests located in tests/5-text_indentation.txt
    checks for type errors
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    for char in ".:?":
        text = text.replace(char, char + "\n\n")
    print("\n".join(line.strip() for line in text.split("\n")), end="")
