import json
import os
import models  # Importa el módulo 'models' si es necesario

class FileStorage:
    __file_path = 'file.json'
    __objects = {}  # Coloca aquí el atributo __objects como se especificó

    def all(self):
        """Devuelve un diccionario con todas las instancias guardadas"""
        return self.__objects

    def new(self, obj):
        """Agrega una nueva instancia al diccionario __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Guarda las instancias en un archivo JSON"""
        objects_dict = {key: obj.to_dict() for key, obj in self.__objects.items()}
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(objects_dict, file)

    def reload(self):
        """Carga las instancias desde el archivo JSON"""
        try:
            with open(FileStorage.__file_path, 'r') as file:
                objects_dict = json.load(file)
                for obj_id, obj_data in objects_dict.items():
                    class_name = obj_data.pop('__class__', None)
                    if class_name and class_name in models.BaseModel.__subclasses__():
                        cls = models.BaseModel.__subclasses__[class_name]
                        obj = cls(**obj_data)
                        self.__objects[obj_id] = obj
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Elimina un objeto de __objects si está presente"""
        if obj:
            key = f"{obj.__class__.__name__}.{obj.id}"
            self.__objects.pop(key, None)  # Usa pop para eliminar de __objects

    def close(self):
        """Llama al método save() para guardar los cambios antes de terminar el programa"""
        self.save()

