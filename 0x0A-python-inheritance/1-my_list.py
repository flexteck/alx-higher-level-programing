#!/usr/bin/python3
class MyList(list):
    """
        A custom list that inherits from the built-in list 
        class.
    """

    def print_sorted(self):
        """prints the list in ascending order"""
        print(sorted(self))
