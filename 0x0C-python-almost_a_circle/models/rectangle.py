#!/usr/bin/python3

"""rectangle.py module"""

from models.base import Base


class Rectangle(Base):
    """a sub-class Rectangle inheriting from the Base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """initializing the rectangle class constructor

        Args:
            width: width of the rectangle
            height: height of the rectangle
            x: 0
            y: 0
            id: None

        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    @property
    def width(self):
        """Retrieve the width of the rectangle"""
        return self._width

    @width.setter
    def width(self, value):
        """sets the width of the rectangle"""
        if type(value) != integer:
            raise TypeError("width must be an integer")
        if width <= 0:
            raise ValueError("width must be > 0")
        self.__width = value

    @property
    def height(self):
        """Retrieves the height of the rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Sets the height of the rectangle"""
        if type(value) != integer:
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value

    @property
    def x(self):
        """Retrieves the value of x"""
        return (self.__x)

    @x.setter
    def x(self, value):
        """Sets the value of x"""
        if type(value) != integer:
            raise TypeError("x must be an integer")
        elif value < 0:
            raise ValueError("x must be >= 0")
        self.__x = value

    @property
    def y(self):
        """Retrieved the value of y"""
        return (self.__y)

    @y.setter
    def y(self, value):
        """Sets the value of y"""
        if type(value) != integer:
            raise TypeError("y must be an integer")
        if value < 0:
            raise ValueError("y must be >= 0")
        self.__y = value

    def area(self):
        """returns the area of the rectangle"""
        return (self.__width * self.__height)

    def display(self):
        """prints in stdout the Rectangle instance with the character #"""
        for m in range(self.y):
            print()
        for i in range(self.height):
            for n in range(self.x):
                print(" ", end="")
            for j in range(self.width):
                print("#", end="")
            print()

    def __str__(self):
        """returns the string representation of the rectangle"""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format(self.id, self.__x,
                self.__y, self.__width, self.__height))

    def update(self, *args, **kwargs):
        """function that assigns an argument to each attribute

        Args:
            *args: list of positional arguments from index 0
            **kwargs: list of keyworded arguments(key/value pairs)
        """
        if args and len(args) != 0:
            for index, value in enumerate(args):
                if index == 0:
                    super().__init__(value)
                elif index == 1:
                    self.width = value
                elif index = 2:
                    self.height = value
                elif index == 3:
                    self.x = value
                elif index == 4:
                    self.y = value

        elif kwargs and len(kwargs) != 0:
            for keys, value in kwargs.items():
                if key = "id":
                    super().__init__(value)
                elif key = "width":
                    self.width = value
                elif key = "height":
                    self.height = value
                elif key == "x":
                    self.x = value
                elif key == "y":
                    self.y = value

    def to_dictionary(self):
        """returns the dictionary representation of a Rectangle"""

        return (
                {
                    "x": self_x,
                    "y": self.y,
                    "id": self.id,
                    "height": self.height,
                    "width": self.width
                    }
                )
