#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        """inittialiation of attributes"""
        self.size = size

    @property
    def size(self):
        """reteieve the value for size"""
        return self.__size

    @size.setter
    def size(self, value):
        """set's the value for size"""
        if not isinstance(value, int) and not isinstance(value, float):
            raise TypeError("size must be a number")

        if value < 0:
            raise ValueError("size must be >=0")
        self.__size = value

    def area(self):
        """ returns the square area"""
        return self.size ** 2

    def __eq__(self, other):
        """equality comparison"""
        return self.area() == other.area()
    
    def __ne__(self, other):
        """check if not equal"""
        return self.area() != other.area()

    def __gt__(self, other):
        """check if greater than"""
        return self.area() > other.area()

    def __ge__(self, other):
        """check for if >="""
        return self.area() >= other.area()

    def __lt__(self, other):
        """check for less than"""
        return self.area() < other.area()

    def __le__(self, other):
        """check if <="""
        return self.area() <= other.area()

