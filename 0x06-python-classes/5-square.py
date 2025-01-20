#!/usr/bin/python3
class Square:
    def __init__(self, size=0):
        self.size = size

    @property
    def size(self):
        """retrieve the size"""
        return self.__self

    @size.setter
    def size(self, value):
        """set size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        
        if value < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = value

    def area(self):
        """return area of a square"""
        return self.__size ** 2

    def my_print(self):
        """print square with #"""
        if self.__size == 0:
            print()
        else:
            for i in range(self.__size):
                print("#" * self.__size)
