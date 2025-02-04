#!/usr/bin/python3
"""
python program
"""


def inherits_from(obj, a_class):
    """
    this is method
    """
    mo_type = type(obj)

    if type(obj) is a_class:
        return False
    if a_class in mo_type.__mro__:
        return True
