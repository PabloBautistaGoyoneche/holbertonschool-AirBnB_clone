#!/usr/bin/python3
"""We test te class Place and all its functions"""
import unittest
from models.place import Place
from models.base_model import BaseModel
from datetime import datetime


class TestPlace(unittest.TestCase):
    """ Test cases for Place class """

    def test_instantiation(self):
        """ Test instantiation """
        place = Place()
        self.assertIsInstance(place, BaseModel)
        self.assertIsInstance(place, Place)
        self.assertEqual(place.city_id, "")
        self.assertEqual(place.user_id, "")
        self.assertEqual(place.name, "")
        self.assertEqual(place.description, "")
        self.assertEqual(place.number_rooms, 0)
        self.assertEqual(place.number_bathrooms, 0)
        self.assertEqual(place.max_guest, 0)
        self.assertEqual(place.price_by_night, 0)
        self.assertEqual(place.latitude, 0.0)
        self.assertEqual(place.longitude, 0.0)
        self.assertEqual(place.amenity_ids, [])

    def test_to_dict(self):
        """ Test to_dict method """
        place = Place()
        place_dict = place.to_dict()
        self.assertEqual(place_dict['__class__'], 'Place')
        self.assertEqual(type(place_dict['created_at']), str)
        self.assertEqual(type(place_dict['updated_at']), str)

    def test_from_dict(self):
        """ Test from_dict method """
        data = {
            'id': '123',
            'city_id': '456',
            'user_id': '789',
            'name': 'Test Place',
            'description': 'Test description',
            'number_rooms': 3,
            'number_bathrooms': 2,
            'max_guest': 6,
            'price_by_night': 100,
            'latitude': 123.45,
            'longitude': -67.89,
            'amenity_ids': ['a1', 'a2']
        }
        place = Place(**data)
        self.assertEqual(place.id, '123')
        self.assertEqual(place.city_id, '456')
        self.assertEqual(place.user_id, '789')
        self.assertEqual(place.name, 'Test Place')
        self.assertEqual(place.description, 'Test description')
        self.assertEqual(place.number_rooms, 3)
        self.assertEqual(place.number_bathrooms, 2)
        self.assertEqual(place.max_guest, 6)
        self.assertEqual(place.price_by_night, 100)
        self.assertEqual(place.latitude, 123.45)
        self.assertEqual(place.longitude, -67.89)
        self.assertEqual(place.amenity_ids, ['a1', 'a2'])


if __name__ == "__main__":
    unittest.main()
