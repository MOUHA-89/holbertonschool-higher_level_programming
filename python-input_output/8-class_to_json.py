#!/usr/bin/python3
"""
python program
"""


def class_to_json(obj):
    """
    function that returns the dictionary for JSON serialization of an object.
    """
    return obj.__dict__
