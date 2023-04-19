#!/usr/bin/python3
"""
Base class
"""


import json


class Base:
    """Base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """Dictionary to JSON string"""
        if list_dictionaries is None:
            return "[]"
        else:
            return json.dumps(list_dictionaries)

    @classmethod
    def save_to_file(cls, list_objs):
        """
        the JSON string to a file
        """
        filename = cls.__name__ + ".json"

        with open(filename, "w", encoding="utf-8") as f:
            if list_objs is None:
                f.write("[]")
            else:
                new_list = [ins.to_dictionary() for ins in list_objs]
                f.write(cls.to_json_string(new_list))

    @staticmethod
    def from_json_string(json_string):
        """
        the JSON string to dictonary
        """
        if json_string is None or len(json_string) == 0:
            return []
        else:
            return json.loads(json_string)

    @classmethod
    def create(cls, **dictionary):
        """Dictionary to instance"""
        if cls.__name__ == "Rectangle":
            dummy_obj = cls(4, 5)  # dummy instance
        if cls.__name__ == "Square":
            dummy_obj = cls(4)  # dummy instance
        dummy_obj.update(**dictionary)
        return dummy_obj

    @classmethod
    def load_from_file(cls):
        """File to instance"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                a_list = cls.from_json_string(f.read())
                return [cls.create(**item) for item in a_list]
        except:
            return []
