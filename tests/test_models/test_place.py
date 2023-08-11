#!/usr/bin/python3
"""We test te class Place and all its functions"""
import unittest
import datetime
from models.base_model import BaseModel
from models.place import Place


class TestPlace(unittest.TestCase):
    def test_inheritance(self):
        # Asegurarse de que Place es una subclase de BaseModel
        self.assertTrue(issubclass(Place, BaseModel))

    def test_attribute_initialization(self):
        instance = Place()

        # Asegurarse de que los atributos estén inicializados correctamente
        self.assertEqual(instance.city_id, "")
        self.assertEqual(instance.user_id, "")
        self.assertEqual(instance.name, "")
        self.assertEqual(instance.description, "")
        self.assertEqual(instance.number_rooms, 0)
        self.assertEqual(instance.number_bathrooms, 0)
        self.assertEqual(instance.max_guest, 0)
        self.assertEqual(instance.price_by_night, 0)
        self.assertEqual(instance.latitude, 0.0)
        self.assertEqual(instance.longitude, 0.0)
        self.assertEqual(instance.amenity_ids, [])

    def test_attribute_manipulation(self):
        instance = Place()

        # Modificar valores de atributos
        instance.city_id = "city_123"
        instance.name = "Sample Place"
        instance.number_rooms = 3
        instance.number_bathrooms = 2
        instance.max_guest = 6
        instance.price_by_night = 150
        instance.latitude = 37.7749
        instance.longitude = -122.4194

        # Asegurarse de que los atributos se hayan actualizado correctamente
        self.assertEqual(instance.city_id, "city_123")
        self.assertEqual(instance.name, "Sample Place")
        self.assertEqual(instance.number_rooms, 3)
        self.assertEqual(instance.number_bathrooms, 2)
        self.assertEqual(instance.max_guest, 6)
        self.assertEqual(instance.price_by_night, 150)
        self.assertEqual(instance.latitude, 37.7749)
        self.assertEqual(instance.longitude, -122.4194)

    def test_attribute_types(self):
        instance = Place()

        # Asegurarse de que los atributos son del tipo esperado
        self.assertIsInstance(instance.id, str)
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertIsInstance(instance.city_id, str)
        self.assertIsInstance(instance.user_id, str)
        self.assertIsInstance(instance.name, str)
        self.assertIsInstance(instance.description, str)
        self.assertIsInstance(instance.number_rooms, int)
        self.assertIsInstance(instance.number_bathrooms, int)
        self.assertIsInstance(instance.max_guest, int)
        self.assertIsInstance(instance.price_by_night, int)
        self.assertIsInstance(instance.latitude, float)
        self.assertIsInstance(instance.longitude, float)
        self.assertIsInstance(instance.amenity_ids, list)

    def test_save(self):
        instance = Place()
        original_updated_at = instance.updated_at
        instance.save()
        self.assertGreater(instance.updated_at, original_updated_at)
        # Asegurarse de que se llame a models.storage.save() en save()

    def test_to_dict(self):
        instance = Place()
        instance_dict = instance.to_dict()
        self.assertIn("id", instance_dict)
        self.assertIn("created_at", instance_dict)
        self.assertIn("updated_at", instance_dict)
        self.assertIn("__class__", instance_dict)
        self.assertTrue(isinstance(instance_dict["created_at"], str))
        self.assertTrue(isinstance(instance_dict["updated_at"], str))
        self.assertEqual(instance_dict["__class__"], "Place")
        self.assertIn("city_id", instance_dict)
        self.assertIn("user_id", instance_dict)
        self.assertIn("name", instance_dict)
        self.assertIn("description", instance_dict)
        self.assertIn("number_rooms", instance_dict)
        self.assertIn("number_bathrooms", instance_dict)
        self.assertIn("max_guest", instance_dict)
        self.assertIn("price_by_night", instance_dict)
        self.assertIn("latitude", instance_dict)
        self.assertIn("longitude", instance_dict)
        self.assertIn("amenity_ids", instance_dict)

    def test_instance_equality(self):
        instance1 = Place(city_id="city_1", name="Place A")
        instance2 = Place(city_id="city_2", name="Place B")
        instance3 = Place(city_id="city_1", name="Place A")

        # Asegurarse de que las instancias se pueden comparar correctamente
        self.assertNotEqual(instance1, instance2)
        self.assertEqual(instance1, instance3)

    def test_init_with_kwargs(self):
        data = {
            "id": "test_id",
            "created_at": "2023-08-10T10:00:00.000000",
            "updated_at": "2023-08-10T11:00:00.000000",
            "city_id": "city_123",
            "user_id": "user_456",
            "name": "Test Place",
            "description": "This is a test place",
            "number_rooms": 2,
            "number_bathrooms": 1,
            "max_guest": 4,
            "price_by_night": 120,
            "latitude": 34.0522,
            "longitude": -118.2437,
            "amenity_ids": ["amenity_1", "amenity_2"]
        }
        instance = Place(**data)
        self.assertEqual(instance.id, "test_id")
        self.assertIsInstance(instance.created_at, datetime.datetime)
        self.assertIsInstance(instance.updated_at, datetime.datetime)
        self.assertEqual(instance.city_id, "city_123")
        self.assertEqual(instance.user_id, "user_456")
        self.assertEqual(instance.name, "Test Place")
        self.assertEqual(instance.description, "This is a test place")
        self.assertEqual(instance.number_rooms, 2)
        self.assertEqual(instance.number_bathrooms, 1)
        self.assertEqual(instance.max_guest, 4)
        self.assertEqual(instance.price_by_night, 120)
        self.assertEqual(instance.latitude, 34.0522)
        self.assertEqual(instance.longitude, -118.2437)
        self.assertEqual(instance.amenity_ids, ["amenity_1", "amenity_2"])


if __name__ == '__main__':
    unittest.main()
