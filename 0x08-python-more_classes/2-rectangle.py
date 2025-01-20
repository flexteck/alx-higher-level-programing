#!/usr/bin/python3
class Rectangle:
    """defines a rectangle"""
    def __init__(self,width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        """retrieves the width"""
        return self.__width

    @width.setter
    def width(self, value):
        """ sets the width value"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        """ retieveds the height"""
        return self.__height

    @height.setter
    def height(self, value):
        """sets value for height"""
        if not isinstance(value, int):
            raise ValueError("height must be an integer")
        if value < 0:
            raise valueError("height must be >= 0")
        self.__height = value 

    def area(self):
        """return the rectangle Area"""
        return self.__width * self.__height

    def perimeter(self):
        """returns the rectangle Perimeter"""
        if self.__width == 0 or self.__height == 0:
            return 0
        return (self.__width * 2) + (self.height * 2)
