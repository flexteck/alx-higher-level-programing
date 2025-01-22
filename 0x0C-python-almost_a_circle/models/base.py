#!/usr/bin/python3
import json

class Base:
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ returns Json string representation of list_dictionaries """

        if list_dictionaries == None or len(list_dictionaries) == 0:
            return "[]"

        return json.dumps(list_dictionaries)