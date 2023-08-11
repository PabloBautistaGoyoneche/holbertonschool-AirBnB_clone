#!/usr/bin/python3
"""We test te class City and all its functions"""
import unittest
import datetime
from models.base_model import BaseModel
from models.city import City


class TestCity(unittest.TestCase):
    def test_inheritance(self):
        # Asegurarse de que City es una subclase de BaseModel
        self.assertTrue(issubclass(City, BaseModel))

    def test_attribute_initialization(self):
        instance = City()

        # Asegurarse de que los atributos state_id y name están
        # inicializados como cadenas vacías
        self.assertEqual(instance.state_id, "")
        self.assertEqual(instance.name, "")

    def test_attribute_manipulation(self):
        instance = City()

        # Modificar el valor del atributo "state_id"
        instance.state_id = "CA"
        self.assertEqual(instance.state_id, "CA")

        # Modificar el valor del atributo "name"
        instance.name = "San Francisco"
        self.assertEqual(instance.name, "San Francisco")

        # Modificar el valor de otro atributo
        instance.other_attr = "Some value"
        self.assertEqual(instance.other_attr, "Some value")

    def test_attribute_types(self):
        instance = City()

        # Asegurarse de que los atributos son del tipo esperado
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.state_id, str)
        self.assertIsInstance(instance.name, str)

    def test_save(self):
        instance = City()
        original_updated_at = instance.updated_at
        instance.save()
        self.assertGreater(instance.updated_at, original_updated_at)
        # Asegurarse de que se llame a models.storage.save() en save()

    def test_to_dict(self):
        instance = City()
        instance_dict = instance.to_dict()
        self.assertIn("id", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)
        self.assertIn("__class__", instance_dict)
        self.assertTrue(isinstance(instance_dict["created_at"], str))
        self.assertTrue(isinstance(instance_dict["updated_at"], str))
        self.assertEqual(instance_dict["__class__"], "City")
        self.assertIn("state_id", instance_dict)
        self.assertIn("name", instance_dict)
        self.assertEqual(instance_dict["state_id"], "")
        self.assertEqual(instance_dict["name"], "")

    def test_instance_equality(self):
        instance1 = City(state_id="CA", name="San Francisco")
        instance2 = City(state_id="CA", name="Los Angeles")
        instance3 = City(state_id="CA", name="San Francisco")

        # Asegurarse de que las instancias se pueden comparar correctamente
        self.assertNotEqual(instance1, instance2)
        self.assertEqual(instance1, instance3)

    def test_init_with_kwargs(self):
        data = {
            "id": "test_id",
            "created_at": "2023-08-10T10:00:00.000000",
            "updated_at": "2023-08-10T11:00:00.000000",
            "state_id": "CA",
            "name": "San Francisco",
            "other_key": "other_value"
        }
        instance = City(**data)
        self.assertEqual(instance.id, "test_id")
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertEqual(instance.state_id, "CA")
        self.assertEqual(instance.name, "San Francisco")
        self.assertEqual(instance.other_key, "other_value")

    def test_string_representation(self):
        instance = City(state_id="CA", name="San Francisco")
        expected_str = "[City] ({}) {}".format(instance.id, instance.__dict__)
        self.assertEqual(str(instance), expected_str)

    def test_to_dict_includes_class_name(self):
        instance = City()
        instance_dict = instance.to_dict()
        self.assertIn("__class__", instance_dict)
        self.assertEqual(instance_dict["__class__"], "City")

    def test_to_dict_and_back(self):
        instance = City(state_id="CA", name="San Francisco")
        instance_dict = instance.to_dict()
        new_instance = City(**instance_dict)
        self.assertEqual(instance.__dict__, new_instance.__dict__)


if __name__ == '__main__':
    unittest.main()
