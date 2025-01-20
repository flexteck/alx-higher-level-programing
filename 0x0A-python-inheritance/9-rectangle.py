#!/usr/bin/python3
BaseGeometry = __import__('7-base_geometry').BaseGeometry

class Rectangle(BaseGeometry):
    """ inherits from BaseGeometry class """

    def __init__(self, width, height):
        """initializing the properties"""

        super().integer_validator("width", width)
        super().integer_validator("height", height)
        self.__width = width
        self.__height = height

    def area(self):
        """ calculates the area of a triangle """
        return self.__width * self.__height

    def __str__(self):
        """ returns rectangle description """
        return f"[Rectangle] {self.__width}/{self.__height}"
