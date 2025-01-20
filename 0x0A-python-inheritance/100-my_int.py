#!/usr/bin/python3
class MyInt(int):
    """A class that inherits front the int class 
    """

    def __eq__(self, other):
        """ overrides == operator to behave != operator """
        return super().__ne__(other)

    def __ne__(self, other):
        """ overides != operator to behave like == operator"""
        return super().__eq__(other)
