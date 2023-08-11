#!/usr/bin/python3
"""We test te class Review and all its functions"""
import unittest
import datetime
from models.base_model import BaseModel
from models.review import Review


class TestReview(unittest.TestCase):
    def test_inheritance(self):
        # Asegurarse de que Review es una subclase de BaseModel
        self.assertTrue(issubclass(Review, BaseModel))

    def test_attribute_initialization(self):
        instance = Review()

        # Asegurarse de que los atributos estén inicializados correctamente
        self.assertEqual(instance.place_id, "")
        self.assertEqual(instance.user_id, "")
        self.assertEqual(instance.text, "")

    def test_attribute_manipulation(self):
        instance = Review()

        # Modificar valores de atributos
        instance.place_id = "place_123"
        instance.text = "This is a sample review."

        # Asegurarse de que los atributos se hayan actualizado correctamente
        self.assertEqual(instance.place_id, "place_123")
        self.assertEqual(instance.text, "This is a sample review.")

    def test_attribute_types(self):
        instance = Review()

        # Asegurarse de que los atributos son del tipo esperado
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.place_id, str)
        self.assertIsInstance(instance.user_id, str)
        self.assertIsInstance(instance.text, str)

    def test_save(self):
        instance = Review()
        original_updated_at = instance.updated_at
        instance.save()
        self.assertGreater(instance.updated_at, original_updated_at)
        # Asegurarse de que se llame a models.storage.save() en save()

    def test_to_dict(self):
        instance = Review()
        instance_dict = instance.to_dict()
        self.assertIn("id", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)
        self.assertIn("__class__", instance_dict)
        self.assertTrue(isinstance(instance_dict["created_at"], str))
        self.assertTrue(isinstance(instance_dict["updated_at"], str))
        self.assertEqual(instance_dict["__class__"], "Review")
        self.assertIn("place_id", instance_dict)
        self.assertIn("user_id", instance_dict)
        self.assertIn("text", instance_dict)
        self.assertEqual(instance_dict["place_id"], "")
        self.assertEqual(instance_dict["user_id"], "")
        self.assertEqual(instance_dict["text"], "")

    def test_instance_equality(self):
        instance1 = Review(place_id="place_1", text="Review A")
        instance2 = Review(place_id="place_2", text="Review B")
        instance3 = Review(place_id="place_1", text="Review A")

        # Asegurarse de que las instancias se pueden comparar correctamente
        self.assertNotEqual(instance1, instance2)
        self.assertEqual(instance1, instance3)

    def test_init_with_kwargs(self):
        data = {
            "id": "test_id",
            "created_at": "2023-08-10T10:00:00.000000",
            "updated_at": "2023-08-10T11:00:00.000000",
            "place_id": "place_123",
            "user_id": "user_456",
            "text": "Test review",
            "other_key": "other_value"
        }
        instance = Review(**data)
        self.assertEqual(instance.id, "test_id")
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertEqual(instance.place_id, "place_123")
        self.assertEqual(instance.user_id, "user_456")
        self.assertEqual(instance.text, "Test review")


if __name__ == '__main__':
    unittest.main()
