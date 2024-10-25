#!/usr/bin/python3
"""The base class for managing instances and serialization."""
import json
import csv


class Base:
    """A base class that manages ID assignment and serialization."""
    __nb_objects = 0

    def __init__(self, base_id=None):
        """Initializes the Base instance.

        Args:
            base_id : The ID of the instance.
            If not provided, a unique ID is auto assigned.
        """
        if base_id is not None:
            self.id = base_id
        else:
            Base.__nb_objects += 1
            self.id = Base.__nb_objects

    @classmethod
    def create(cls, **dictionary):
        """Returns an instance with all attributes already set."""
        if dictionary and dictionary != {}:
            if cls.__name__ == "Rectangle":
                new = cls(1, 1)  # Placeholder values
            else:
                new = cls(1)  # Placeholder for other classes
            if hasattr(new, 'update'):
                new.update(**dictionary)  # Call update only if it exists
            return new

    @staticmethod
    def to_json_string(list_dictionaries):
        """Returns a JSON str rep of list_dictionaries."""
        if list_dictionaries is None:
            return "[]"
        return json.dumps(list_dictionaries)

    @staticmethod
    def from_json_string(json_string):
        """Returns the list rep by the JSON string."""
        if json_string is None or len(json_string) == 0:
            return []
        return json.loads(json_string)

    @classmethod
    def save_to_file(cls, list_objs):
        """Writes the JSON str rep of list_objs to a file."""
        content = []
        if list_objs is not None:
            for item in list_objs:
                content.append(item.to_dictionary())
        filename = f"{cls.__name__}.json"
        with open(filename, mode='w', encoding='utf-8') as a_file:
            json.dump(content, a_file)

    @classmethod
    def load_from_file(cls):
        """Returns a list of instances loaded from a JSON file."""
        filename = f"{cls.__name__}.json"
        try:
            with open(filename, mode='r', encoding='utf-8') as json_file:
                inst_list = cls.from_json_string(json_file.read())
                return [cls.create(**d) for d in inst_list]
        except IOError:
            return []

    @classmethod
    def save_to_file_csv(cls, list_objs):
        """Serializes list_objs to a CSV file."""
        filename = f"{cls.__name__}.csv"
        with open(filename, mode='w', newline='', encoding='utf-8') as csvfile:
            if list_objs is None or list_objs == []:
                csvfile.write("[]")
            else:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()  # Write header row
                for obj in list_objs:
                    writer.writerow(obj.to_dictionary())

    @classmethod
    def load_from_file_csv(cls):
        """Deserializes instances from a CSV file."""
        filename = f"{cls.__name__}.csv"
        try:
            with open(filename, mode='r', encoding='utf-8') as csvfile:
                if cls.__name__ == "Rectangle":
                    fieldnames = ["id", "width", "height", "x", "y"]
                else:
                    fieldnames = ["id", "size", "x", "y"]
                list_dicts = csv.DictReader(csvfile, fieldnames=fieldnames)
                # Convert strings to integers
                list_dicts = [
                    {k: int(v) for k, v in d.items()} for d in list_dicts
                ]
                return [cls.create(**d) for d in list_dicts]
        except IOError:
            return []
