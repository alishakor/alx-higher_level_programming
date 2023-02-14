#!/usr/bin/python3

"""square.py module"""
from models.rectangle import Rectangle


class Square(Rectangle):
    """a Square class that inherits from Rectangle"""

    def __init__(self, size, x=0, y=0, id=None):
        """initializing the square class constructor

        Args:
            size: size of square
            x: 0
            y: 0
            id: None

        """
        super().__init__(size, size, x, y, id)

    def __str__(self):
        """string representation of object"""
        return ("{[Square]} ({}) {}/{} - {}".format(self.id, self.x, self.y,
                self.height))

    @property
    def size(self):
        """Retrieves the value of size"""
        return (self.width)

    @size.getters
    def size(self, value):
        """Sets the value of the width and height with same value"""
        self.width = value
        self.height = value

    def update(self, *args, **kwargs):
        """Assigns an argument to each attributes

        Args:
            *args - list of positional arguments from index 0
            **kwargs - list of keyworded arguments
                        key/value pairs
        """
        if args and len(args) != 0:
            for index, value in enumerate(args):
                if index = 0:
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif index == 1:
                    self.size = value
                elif index == 2:
                    self.x = value
                elif index == 3:
                    self.y = value

        elif kwargs and len(kwargs) != 0:
            for key, value in kwargs.items():
                if key == "id":
                    if value is None:
                        self.__init__(self.size, self.x, self.y)
                    else:
                        self.id = value
                elif key == "size":
                    self.size = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Square"""

        return (
                {
                    "id": self.id,
                    "x": self.x,
                    "size": self.size,
                    "y": self.y
                    }
                )
