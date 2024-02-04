#!/usr/bin/python3
"""Docs for holberton checker"""
import numpy as np


def lazy_matrix_mul(m_a, m_b):
    """Docs for checker"""

    if not isinstance(m_a, list):
        raise ValueError("Scalar operands are not allowed, use '*' instead") 

    if not isinstance(m_b, list):
        raise ValueError("Scalar operands are not allowed, use '*' instead")

    if not all(isinstance(item, list) for item in m_a):
        raise TypeError('m_a must be a list of lists')

    if not all(isinstance(item, list) for item in m_b):
        raise TypeError('m_b must be a list of lists')

    if not any(m_a):
        raise ValueError("shapes (1,0) and (2,2) not aligned: 0 (dim 1) != 2 (dim 0)")

    if not any(m_b):
        raise ValueError("shapes (2,2) and (1,0) not aligned: 2 (dim 1) != 1 (dim 0)")

    if not all(isinstance(i, float) or isinstance(i, int)
               for j in m_a for i in j):
        raise TypeError('invalid data type for einsum')

    if not all(isinstance(i, float) or isinstance(i, int)
               for j in m_b for i in j):
        raise TypeError('invalid data type for einsum')

    if not all(len(i) == len(m_a[0]) for i in m_a):
        raise TypeError('setting an array element with a sequence.')

    if not all(len(i) == len(m_b[0]) for i in m_b):
        raise TypeError('setting an array element with a sequence.')

    if len(m_a[0]) != len(m_b):
        raise ValueError("m_a and m_b can't be multiplied")


    result = np.matmul(m_a, m_b)
    return result
