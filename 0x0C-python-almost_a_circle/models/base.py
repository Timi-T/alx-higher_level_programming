#!/usr/bin/python3
"""
base class module
"""


import json


class Base:
    """
    base class
    """
    __nb_objects = 0

    def __init__(self, id=None):
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        if (list_dictionaries is None) or (len(list_dictionaries) == 0):
            return "[]"
        dic_str = json.dumps(list_dictionaries)
        return dic_str

    @classmethod
    def save_to_file(cls, list_objs):
        file_name = cls.__name__ + ".json"
        if (list_objs is None) or (len(list_objs) == 0):
            json_str = "[]"
        else:
            list_of_dics = []
            for i in range(len(list_objs)):
                dict_format = list_objs[i].to_dictionary()
                list_of_dics.append(dict_format)
            json_str = cls.to_json_string(list_of_dics)
        with open(file_name, 'w') as f:
            f.write(json_str)

    def from_json_string(json_string):
        if (json_string is None) or (len(json_string) == 0):
            json_list = []
        else:
            json_list = json.loads(json_string)
        return json_list

    @classmethod
    def create(cls, **dictionary):
        r1 = cls(10, 10)
        instances = []
        r1.update(**dictionary)
        return r1

    @classmethod
    def load_from_file(cls):
        instance_list = []
        file_name = cls.__name__ + ".json"
        try:
            with open(file_name, 'r') as f:
                file_content = f.read()
            dict_list = cls.from_json_string(file_content)
            for i in range(len(dict_list)):
                instance = cls.create(**dict_list[i])
                instance_list.append(instance)
        except Exception:
            pass
        return instance_list
