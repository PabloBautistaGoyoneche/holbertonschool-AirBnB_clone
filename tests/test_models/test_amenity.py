#!/usr/bin/python3
"""We test te class Amenity and all its functions"""
import unittest
import datetime
from models.base_model import BaseModel
from models.amenity import Amenity


class TestAmenity(unittest.TestCase):
    def test_inheritance(self):
        # Asegurarse de que Amenity es una subclase de BaseModel
        self.assertTrue(issubclass(Amenity, BaseModel))

    def test_attribute_manipulation(self):
        instance = Amenity()

        # Asegurarse de que el atributo "name" está inicializado
        # como una cadena vacía
        self.assertEqual(instance.name, "")

        # Modificar el valor del atributo "name"
        instance.name = "Test Amenity Name"
        self.assertEqual(instance.name, "Test Amenity Name")

        # Modificar el valor de otro atributo
        instance.other_attr = "Some value"
        self.assertEqual(instance.other_attr, "Some value")

    def test_attribute_types(self):
        instance = Amenity()

        # Asegurarse de que los atributos son del tipo esperado
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.name, str)

    def test_save(self):
        instance = Amenity()
        original_updated_at = instance.updated_at
        instance.save()
        self.assertGreater(instance.updated_at, original_updated_at)
        # Asegurarse de que se llame a models.storage.save() en save()

    def test_to_dict(self):
        instance = Amenity()
        instance_dict = instance.to_dict()
        self.assertIn("id", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)
        self.assertIn("__class__", instance_dict)
        self.assertTrue(isinstance(instance_dict["created_at"], str))
        self.assertTrue(isinstance(instance_dict["updated_at"], str))
        self.assertEqual(instance_dict["__class__"], "Amenity")
        self.assertIn("name", instance_dict)
        self.assertEqual(instance_dict["name"], "")

    def test_instance_equality(self):
        instance1 = Amenity(name="Test Amenity 1")
        instance2 = Amenity(name="Test Amenity 2")
        instance3 = Amenity(name="Test Amenity 1")

        # Asegurarse de que las instancias se pueden comparar correctamente
        self.assertNotEqual(instance1, instance2)
        self.assertEqual(instance1, instance3)

    def test_init_with_kwargs(self):
        data = {
            "id": "test_id",
            "created_at": "2023-08-10T10:00:00.000000",
            "updated_at": "2023-08-10T11:00:00.000000",
            "name": "Test Amenity",
            "other_key": "other_value"
        }
        instance = Amenity(**data)
        self.assertEqual(instance.id, "test_id")
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertEqual(instance.name, "Test Amenity")
        self.assertEqual(instance.other_key, "other_value")


if __name__ == '__main__':
    unittest.main()
