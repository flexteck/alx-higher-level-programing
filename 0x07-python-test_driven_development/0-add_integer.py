#!/usr/bin/python3
def add_integer(a, b=98):
    """
    adds two integers

    raise a TypeError if any of the arguments is neither int
    or float.

    cast a and b to int

    Args:
        a (int or float): first argument
        b (int or float): second argument (default is 98)

    Return:
        int: the sum of a and b as an integer
    """
    if type(a) not in [int, float]:
        raise TypeError("a must be an integer")
    if type(b) not in [int, float]:
         raise TypeError("b must be an integer")
    if isinstance(a, float):
       a = int(a)
    if isinstance(b, float):
         b = int(b)
     
    return a + b
