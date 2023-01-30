#!/usr/bin/python3

"""a class Rectangle that defines a rectangle"""


class Rectangle:
    """define a class rectangle"""

    def __init__(self, width=0, height=0):
        """initializing the Rectangle class

        Args:
            width(int): width of the rectangle
            length(int): length of the rectangle

        Raises:
            TypeError: if width is not an integer
            ValueError: if width is < 0

        """
        self.height = height
        self.width = width

    @property
    def width(self):
        """Retrieves the width of the rectangle"""

        return self.__width

    @width.setter
    def width(self, value):
        """Sets the width of the rectangle"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""

        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value


