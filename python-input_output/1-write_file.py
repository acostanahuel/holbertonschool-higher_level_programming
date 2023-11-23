#!/usr/bin/python3
"""TAsk 1"""


def write_file(filename="", text=""):
    """sds"""
    with open(filename, "w", encoding="utf-8") as file:
        st = file.write(text)
        file.close()
    return(st)