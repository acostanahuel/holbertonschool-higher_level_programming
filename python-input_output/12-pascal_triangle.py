#!/usr/bin/python3
"""pascal triangle"""


def pascal_triangle(n):
    """pascal triangle"""
    lst = []
    if n <= 0:
        return lst

    for i in range(n):
        r = [1]
        if lst:
            r_l = lst[-1]
            r.extend(r_l[j] + r_l[j + 1] for j in range(len(r_l) - 1))
            r.append(1)
        lst.append(r)
    return lst