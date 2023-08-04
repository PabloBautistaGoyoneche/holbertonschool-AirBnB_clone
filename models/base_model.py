import uuid
import datetime
from models import storage  # Se importa el módulo 'storage'

class BaseModel:
    def __init__(self, *args, **kwargs):
        if kwargs:
            for key, value in kwargs.items():
                if key == '__class__':
                    continue
                setattr(self, key, value)
            self.created_at = datetime.datetime.strptime(kwargs.get('created_at', datetime.datetime.now().isoformat()), '%Y-%m-%dT%H:%M:%S.%f')
            self.updated_at = datetime.datetime.strptime(kwargs.get('updated_at', datetime.datetime.now().isoformat()), '%Y-%m-%dT%H:%M:%S.%f')
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.datetime.now()
            self.updated_at = self.created_at
            storage.new(self)  # Llamada al método new(self) en storage para instancias nuevas

    def save(self):
        """Actualiza el atributo updated_at con la fecha y hora actual"""
        self.updated_at = datetime.datetime.now()
        storage.save()  # Llamada al método save(self) de storage

    def to_dict(self):
        """Convierte los atributos de la clase en un diccionario"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

