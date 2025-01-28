#!/usr/bin/python3
"""
this is programm python
"""


class Rectangle:
    """
    A class that defines a rectangle by its width and heigth
    """
    def __init__(self, width=0, heigth=0):
        """
        initialize a new rectangle instance

        Args:
        width (int): the width of the rectangle's side.
        heigth (int): the heigth of the rectangle's side.
        """

        self.width = width
        self.heigth = heigth

        @property
        def width(self):
            """
            retrieves the width of the rectangle
            returns:
            int: the width of the rectangle's side
            """

            return self.__width

        @width.setter
        def width(self, value):
            """"
            sets the size of the rectangle
            Args:
            width(int): the width of the rectangle's side
            raise:
                   TypeError: if value is not an integer
                   ValueError: if value is less than 0
            """
            if not isinstance(width, int):
                raise TypeError("width must be an integer")

            if width < 0:
                raise ValueError("width must be >= 0")

            self.__value = value

        @property
        def heigth(self):
            """
            retrieves the heigth of the rectangle
            returns:
                int: the heigth of the rectangle's side
            """

            return self.__heigth

        @heigth.setter
        def heigth(self, value):
            """"
            sets the heigth of rectangle
            Args:
            heigth(int): the heigth of the rectangle's side
            self.__heigth = value
            raise:
                    TypeError: if value is not an integer
                    ValueError: if value is less than 0
            """
            if not isinstance(heigth, int):
                raise TypeError("height must be an integer")

            if heigth < 0:
                raise ValueError("height must be >= 0")
            self.__heigth = heigth
