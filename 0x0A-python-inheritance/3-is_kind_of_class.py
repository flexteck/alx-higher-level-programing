#!/usr/bin/bash/python3

def is_kind_of_class(obj, a_class):
    """ returns true if the object is an instance of, or
        if the object is an instance of a class that inherited
        from specified class
    """
    return isinstance(obj, a_class)
