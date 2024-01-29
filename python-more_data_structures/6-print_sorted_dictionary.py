#!/usr/bin/python3
def print_sorted_dictionary(a_dictionary: dict()) -> dict():
     for key, val in sorted(a_dictionary.items()):
         print("{}: {}".format(key, val))
