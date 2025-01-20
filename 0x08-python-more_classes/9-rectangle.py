#!/usr/bin/python3
class Rectangle:
    """defines a rectangle"""

    number_of_instance = 0
    print_symbol = "#"

    def __init__(self,width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instance +=1

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

    def __str__(self):
        """print rectangle with #"""
        if self.__width == 0 or self.__height == 0:
            return ""

        rect = "\n".join(str(self.print_symbol) * self.__width for _ in range(self.__height))

        return rect

    def __repr__(self):
        """ return a string representatio of the rectangle"""
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        """print a message"""
        Rectangle.number_of_instance -= 1
        print("Bye rectangle...")

    @staticmethod
    def validate_Rectangle(rect_1, rect_2):
        """check if rect1 or rect2 is an instance
            of the rectangle class
        """
        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

    @staticmethod
    def bigger_or_equal(rect_1, rect_2):
        """returns the biggest rectangle based on the area"""
        Rectangle.validate_Rectangle(rect_1, rect_2)

        if rect_1.area() > rect_2.area():
            return rect_1
        elif rect_2.area() > rect_1.area():
            return rect_2
        else:
            return rect_1

    @classmethod
    def square(cls, size=0):
        """returns new rectangle instance"""
        width = height = size
        return cls(width, height)
