#!/usr/bin/python3

class Student:
    """A class that defines students"""
    def __init__(self, first_name, last_name, age):
        """initialization ofattributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self, attrs=None):
        """return dict of all instance"""
        
        if attrs == None:
            return self.__dict__
        if isinstance(attrs, list) and all(isinstance(attr, str) for attr in attrs):
            return {key : value for key, value in self.__dict__.items() if key in attrs}

        return self.__dict__
