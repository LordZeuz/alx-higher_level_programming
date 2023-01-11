#!/usr/bin/python3
"""module contains a function that write
   a string to a text file(UTF-8)
"""


def write_file(filename="", text=""):
    """write a string to a text file"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
