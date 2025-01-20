#!/usr/bin/bash/python3

def is_same_class(obj, a_class):
    """ return True if the object is an instance of the 
        specified class
    """
    if type(obj) == a_class:
        return True
    else:
        return False
