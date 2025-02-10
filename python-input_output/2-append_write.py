#!/usr/bin/python3
"""
python program
"""


def append_write(filename="", text=""):
    """
    Reads a UFT-8 encoded a file text and return its content to stdout.
    """

    with open(filename, "a", encoding="UTF-8") as file:
        return file.write(text)
