#!/usr/bin/python3

class Student:
    """A class that defines students"""
    def __init__(self, first_name, last_name, age):
        """initialization ofattributes"""
        self.first_name = first_name
        self.last_name = last_name
        self.age = age


    def to_json(self):
        """return dict of all instance"""
        return self.__dict__
