#!/usr/bin/python3
def add_attribute(obj, name, value):
    """ add attribute to a class"""
    if not hasattr(obj, "__dict__"):
        raise TypeError("cant add new attribute")
    setattr(obj, name, value)
