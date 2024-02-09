#!/usr/bin/python3
"""Docs for holberton checker"""


def pascal_triangle(n):
    """Docs for holberton checker"""

    if n <= 0:
        return []

    triangle = [[1]]
    for i in range(1, n):
        row = [1]
        last_row = triangle[-1]
        row += [sum(pair) for pair in zip(last_row, last_row[1:])]
        row.append(1)
        triangle.append(row)
    return triangle
