#!/usr/bin/python3

def inherits_from(obj, a_class):
    """ return True if the object is an instance of a class
        inherited (directly or indirectly) from the specified
        classs
    """
    return isinstance(obj, a_class) and type(obj) != a_class
