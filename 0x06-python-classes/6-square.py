#!/usr/bin/python3

"""A class that defines a square"""


class Square:
    """A class that represents a square"""

    def __init__(self, size=0):
        """Initializing the square class

        Args:
            size(int): represents the size of the square defined

        Raises:
            TypeError: if size is not an integer
            ValueError: if size is less than 0
        """

        if type(size) is not int:
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    @property
    def size(self):
        """class method that retrieve a private instance attribute"""

        return self.__size

    @size.setter
    def size(self, value):
        if type(value) is not int:
            raise TypeError('size must be an integer')
        if value < 0:
            raise ValueError('size must be >= 0')
        self.__size = value

    def area(self):
        """ Class method that calculates the area of square

        Returns: The square of size
        """

        return self.__size ** 2

    @property
    def position(self):
        """property method to retrieve position"""
        return (self.__position)

    @position.setter
    def position(self, value):
        if (not isinstance(value, tuple) or
                len(value) != 2 or
                not all(isinstance(i, int) for i in value) or
                not all(i >= 0 for i in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def my_print(self):
        """ class method that prints a square"""
        if (self.__size == 0):
            print("")
        else:
            [print("") for i in range(self.__position[1])]
            for x in range(self.__size):
                for i in range(self.__position[0]):
                    print(" ", end="")
                for y in range(self.__size):
                    print("#", end="")
                print("")
