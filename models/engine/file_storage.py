import json
import os
from models.base_model import BaseModel

class FileStorage:
    __file_path = 'file.json'
    __objects = {} 

    def all(self):
        return self.__objects
    
    def new(self, obj):
        """ Add a new instance to the __objects dictionary """
        if obj:
            key = '{}.{}'.format(obj.__class__.__name__, obj.id)
            self.__objects[key] = obj

    def save(self):
        """ Save the instances in a JSON file """
        data = {}
        for k, v in self.__objects.items():
            data[k] = v.to_dict()
        with open(self.__file_path, 'w') as f:
            json.dump(data, f)

    def reload(self):
        """ Load the instances from the JSON file """
        classes = {"BaseModel": BaseModel}
        try:
            with open(self.__file_path, 'r') as f:
                data = f.read()
                data = json.loads(data)
                for k, v in data.items():
                    self.__objects[k] = classes[v["__class__"]](**v)
        except FileNotFoundError:
            pass

    def delete (self, obj=None):
        """ Removes an object from __objects if it is present """
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects.pop(key, None) 

    def close(self):
        """ Call the save() method to save the changes before terminating the program. """
        self.save()

