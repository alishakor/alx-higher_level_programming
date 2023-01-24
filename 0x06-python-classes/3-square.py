#!/usr/bin/python3

"""a class that creates a square"""

class Square:
    """the square class"""

    def __init__(self, size=0):
        """initialize a new square

        Args:
            size (init): the size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size

    def area(self):
        """class method that calculates area of square"
        returns:
            result
        """

        result = self.__size * self.__size

        return (result)
