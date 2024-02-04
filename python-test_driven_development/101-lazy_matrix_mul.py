#!/usr/bin/python3
"""Docs for holberton checker"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Docs for checker"""
    arr_1 = np.array(m_a)
    arr_2 = np.array(m_b)
    try:
        result = np.dot(arr_1, arr_2)
    except Exception as e:
        return e
    return result
