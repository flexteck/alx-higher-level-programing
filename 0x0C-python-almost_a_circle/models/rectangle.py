#!/usr/bin/python3
from models.base import Base

class Rectangle(Base):

    def __init__(self, width, height, x=0, y=0, id=None):
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        "Overiding the __str__ method"
        return f"[Rectangle] ({self.id}) {self.__x} / {self.__y} - {self.__width} / {self.__height} "

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        self.validate_attributes('width', value)
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        self.validate_attributes('height', value)
        self.__height = value

    @property
    def x(self):
        return self.__x

    @x.setter
    def x(self, value):
        self.validate_non_negative('x', value)
        self.__x = value

    @property
    def y(self):
        return self.__y

    @y.setter
    def y(self, value):
        self.validate_non_negative('y', value)
        self.__y = value

    @staticmethod
    def validate_attributes(attribute, value):
        if not isinstance(value, int):
            raise TypeError(f"{attribute} must be an integer")

        if value <= 0:
            raise ValueError(f"{attribute} must be > 0")
    
    @staticmethod
    def validate_non_negative(attribute, value):
        if type(value) is not int:
            raise TypeError(f"{attribute} must be an integer")

        if value < 0:
            raise ValueError(f"{attribute} must be >= 0")


    def area(self):
        "return's the area value of a Rectangle"
        return self.__width * self.__height


    def display(self):
        "use '#' to print the Rectangle to stdout, respecting x and y coordinate"
        print('\n' * self.__y, end="")

        for _ in range(self.__height):
            print(" " * self.__x + '#' * self.__width)

    def update(self, *args):
        """Updates the rectangle attributes using positional arguments.
        Arguments are assigned in the following order:
        1st argument -> id
        2nd argument -> width
        3rd argument -> height
        4th argument -> x
        5th argument -> y
        """

        attributes = ["id", "width", "height", "x", "y"]

        for i, value in enumerate(args):
            if i < len(attributes):
                setattr(self, attributes[i], value)
