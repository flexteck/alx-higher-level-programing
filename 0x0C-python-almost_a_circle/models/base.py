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

    @classmethod
    def save_to_file(cls, list_objs):
        
        filename = f"{cls.__name__}.json"

        with open(filename, "w", encoding="utf-8") as file:
            if list_objs is None or len(list_objs) == 0:
                file.write("[]")
            else:
                list_dict = [obj.to_dictionary() for obj in list_objs]
                json_string = cls.to_json_string(list_dict)
                file.write(json_string)

    
    @staticmethod
    def from_json_string(json_string):
        if json_string == None or len(json_string) == 0:
            return "[]"

        return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 1)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        else:
            raise ValueError("Unsupported class ")

        dummy.update(**dictionary)

        return dummy