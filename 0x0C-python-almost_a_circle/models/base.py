#!/usr/bin/python3
"""The first class which will be a Base class """
import json
import csv


class Base:
    """ A base class"""
    __nb_objects = 0

    def __init__(self, id=None):
        """ initialization or instantation of the class"""
        if id is not None:
            self.id = id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """ returns an instance with all attributes already set: """
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)
            else:
                new = cls(1)
            new.update(**dictionary)
            return new

    @staticmethod
    def to_json_string(list_dictionaries):
        """ return a json rep of the dico """
        if list_dictionaries is None:
            return "[]"

        list_Json = json.dumps(list_dictionaries)
        return list_Json

    @staticmethod
    def from_json_string(json_string):
        """ returns the list of the JSON string representation json_string"""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """ writes JSON string rep of list_objs to a file """
        content = []
        if list_objs is not None:
            for item in list_objs:
                item = item.to_dictionary()
                json_dict = json.loads(cls.to_json_string(item))
                content.append(json_dict)
        file_name = cls.__name__ + ".json"
        with open(file_name, mode='w', encoding='utf-8') as a_file:
            json.dump(content, a_file)

    @classmethod
    def load_from_file(cls):
        """ returns a list of instances"""
        filename = cls.__name__ + ".json"
        try:
            with open(filename, mode='r', encoding='utf-8') as json_file:
                inst_list = Base.from_json_string(json_file.read())
                return [cls.create(**d) for d in inst_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """ serailizes in csv """
        filename = cls.__name__ + ".csv"
        with open(filename, mode='w', encoding='utf-8') as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """ deserialize"""
        filename = cls.__name__ + ".csv"
        try:
            with open(filename, mode='r', encoding='utf-8') as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames)
                list_dicts = [dict([k, int(v)] for k, v in d.items())
                              for d in list_dicts]
                return [cls.create(**d) for d in list_dicts]

        except IOError:
            return []
