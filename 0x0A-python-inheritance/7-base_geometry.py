#!/usr/bin/python3
class BaseGeometry:
    """ Base class """
    def area(self):
        """ raises exception"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """ validates value"""
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")

        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
