#!/usr/bin/python3
"""
python programm
"""


class MyList(list):
    """
    this is class that define a list
    """
    def print_sorted(self):
        sorted_list = sorted(self)
        print(sorted_list)
