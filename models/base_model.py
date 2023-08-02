import uuid
import datetime

class BaseModel:
    def __init__(self):
        self.id = str(uuid.uuid4())
        # Genera un ID único usando uuid4 y lo convierte a string
        self.created_at = datetime.datetime.now() 
        # Asigna la fecha y hora actual al atributo created_at
        self.updated_at = self.created_at 
        # Inicialmente, updated_at será igual a created_at

    def __str__(self):
        return f"[{self.__class__.__name__}] ({self.id}) {self.__dict__}"

    def save(self):
        """Actualiza el atributo updated_at con la fecha y hora actual"""
        self.updated_at = datetime.datetime.now()

    def to_dict(self):
        """Convierte los atributos de la clase en un diccionario"""
        obj_dict = self.__dict__.copy()
        obj_dict['__class__'] = self.__class__.__name__
        obj_dict['created_at'] = self.created_at.isoformat()
        obj_dict['updated_at'] = self.updated_at.isoformat()
        return obj_dict
