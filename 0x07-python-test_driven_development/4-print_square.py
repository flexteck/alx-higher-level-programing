#!/usr/bin/python3
def print_square(size):
    """
    prints square with the character #

    Args:
        arg1:
            size(int)

    Return: 
        nothing

    Error:
        raise TypeError if size is not an integer or
        if size is float and < 0

        raise ValueError if size is < 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")

    if size < 0:
        raise ValueError("size must be >= 0")

    if isinstance(size, float) and size < 0:
        raise TypeError("size must be and integer")

    for i in range(size):
        print("#" * size)
