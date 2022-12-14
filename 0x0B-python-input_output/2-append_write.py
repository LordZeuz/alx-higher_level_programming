#!/usr/bin/python3
"""module contains a function that
   appends a str to a text file
"""


def append_write(filename="", text=""):
    """appends a str to a text"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
