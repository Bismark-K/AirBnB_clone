#!/usr/bin/python3
"""File storage's module."""
import json


class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self):
        return self.__objects

    def new(self, obj):
        key = "{} {}".format(obj.__class__.__name__, obj.id)
        self.__objects[key] = obj

    def save(self):
        obj_dict = {}
        for key, obj in self.all().items():
            obj_dict[key] = obj.to_dict()

        with open(self.__file_path, "w", encoding="UTF-8") as test_file:
            json.dump(obj_dict, test_file)

    def reload(self):
        from models.place import Place
        from models.user import User
        from models.base_model import BaseModel
        from models.city import City

        class_map = {
                'BaseModel': BaseModel,
                'User': User,
                'City': City,
                'Place': Place
                }

        try:
            with open(self.__file_path, "r", encoding="UTF-8") as text_file:
                obj_dict = json.load(text_file)

                for key, value in obj_dict.items():
                    class_name = value['__class__']
                    class_instance = class_map[class_name]
                    instance = class_instance(**value)
                    all_objects = self.all()
                    all_objects[key] = instance
        except FileNotFoundError:
            pass
