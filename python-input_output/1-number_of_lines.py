#!/usr/bin/python3
""" saaaaaa """


def write_file(filename="", text=""):
    """sksadapsdas"""
    with open(filename, "w", encoding="utf-8") as file:
        st = file.write(text)
        file.close()
    return(st)