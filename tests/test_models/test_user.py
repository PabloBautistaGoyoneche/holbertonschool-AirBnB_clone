#!/usr/bin/python3
"""We test te class User and all its functions"""
import unittest
import datetime
from models.base_model import BaseModel
from models.user import User


class TestUser(unittest.TestCase):
    def test_inheritance(self):
        # Asegurarse de que User es una subclase de BaseModel
        self.assertTrue(issubclass(User, BaseModel))

    def test_attribute_initialization(self):
        instance = User()

        # Asegurarse de que los atributos estén inicializados correctamente
        self.assertEqual(instance.email, "")
        self.assertEqual(instance.password, "")
        self.assertEqual(instance.first_name, "")
        self.assertEqual(instance.last_name, "")

    def test_attribute_manipulation(self):
        instance = User()

        # Modificar valores de atributos
        instance.email = "test@example.com"
        instance.first_name = "John"
        instance.last_name = "Doe"

        # Asegurarse de que los atributos se hayan actualizado correctamente
        self.assertEqual(instance.email, "test@example.com")
        self.assertEqual(instance.first_name, "John")
        self.assertEqual(instance.last_name, "Doe")

        # Modificar el valor de otro atributo
        instance.other_attr = "Some value"
        self.assertEqual(instance.other_attr, "Some value")

    def test_attribute_types(self):
        instance = User()

        # Asegurarse de que los atributos son del tipo esperado
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.email, str)
        self.assertIsInstance(instance.password, str)
        self.assertIsInstance(instance.first_name, str)
        self.assertIsInstance(instance.last_name, str)

    def test_save(self):
        instance = User()
        original_updated_at = instance.updated_at
        instance.save()
        self.assertGreater(instance.updated_at, original_updated_at)
        # Asegurarse de que se llame a models.storage.save() en save()

    def test_to_dict(self):
        instance = User()
        instance_dict = instance.to_dict()
        self.assertIn("id", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)
        self.assertIn("__class__", instance_dict)
        self.assertTrue(isinstance(instance_dict["created_at"], str))
        self.assertTrue(isinstance(instance_dict["updated_at"], str))
        self.assertEqual(instance_dict["__class__"], "User")
        self.assertIn("email", instance_dict)
        self.assertIn("password", instance_dict)
        self.assertIn("first_name", instance_dict)
        self.assertIn("last_name", instance_dict)
        self.assertEqual(instance_dict["email"], "")
        self.assertEqual(instance_dict["password"], "")
        self.assertEqual(instance_dict["first_name"], "")
        self.assertEqual(instance_dict["last_name"], "")

    def test_instance_equality(self):
        instance1 = User(email="test@example.com", first_name="John")
        instance2 = User(email="another@example.com", first_name="Jane")
        instance3 = User(email="test@example.com", first_name="John")

        # Asegurarse de que las instancias se pueden comparar correctamente
        self.assertNotEqual(instance1, instance2)
        self.assertEqual(instance1, instance3)

    def test_init_with_kwargs(self):
        data = {
            "id": "test_id",
            "created_at": "2023-08-10T10:00:00.000000",
            "updated_at": "2023-08-10T11:00:00.000000",
            "email": "test@example.com",
            "password": "test_password",
            "first_name": "John",
            "last_name": "Doe",
            "other_key": "other_value"
        }
        instance = User(**data)
        self.assertEqual(instance.id, "test_id")
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertEqual(instance.email, "test@example.com")
        self.assertEqual(instance.password, "test_password")
        self.assertEqual(instance.first_name, "John")
        self.assertEqual(instance.last_name, "Doe")
        self.assertEqual(instance.other_key, "other_value")


if __name__ == '__main__':
    unittest.main()
