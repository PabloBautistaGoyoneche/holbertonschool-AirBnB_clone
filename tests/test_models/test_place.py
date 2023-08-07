#!/usr/bin/python3
"""We test te class Place and all its functions"""
import unittest
from datetime import datetime
from models.place import Place


class TestBase(unittest.TestCase):
    """The test class to work in unicode"""

    def testSet(self):
        """Check if you can generate an instance"""
        self.P = Place()

    def testExist(self):
        """A test that check if the attributes exists in the class"""
        P1 = Place()
        self.assertTrue(hasattr(P1, "id"))
        self.assertTrue(hasattr(P1, "created_at"))
        self.assertTrue(hasattr(P1, "updated_at"))
        self.assertTrue(hasattr(P1, "city_id"))
        self.assertTrue(hasattr(P1, "user_id"))
        self.assertTrue(hasattr(P1, "name"))
        self.assertTrue(hasattr(P1, "description"))
        self.assertTrue(hasattr(P1, "number_rooms"))
        self.assertTrue(hasattr(P1, "number_bathrooms"))
        self.assertTrue(hasattr(P1, "max_guest"))
        self.assertTrue(hasattr(P1, "price_by_night"))
        self.assertTrue(hasattr(P1, "latitude"))
        self.assertTrue(hasattr(P1, "longitude"))
        self.assertTrue(hasattr(P1, "amenity_ids"))

    def testUser(self):
        """A test to check if all values are the correct type"""
        P2 = Place
        self.assertIsInstance(P2.id, str)
        self.assertIsInstance(P2.created_at, datetime)
        self.assertIsInstance(P2.updated_at, datetime)
        self.assertIsInstance(P2.city_id, str)
        self.assertIsInstance(P2.user_id, str)
        self.assertIsInstance(P2.name, str)
        self.assertIsInstance(P2.description, str)
        self.assertIsInstance(P2.number_rooms, int)
        self.assertIsInstance(P2.number_bathrooms, int)
        self.assertIsInstance(P2.max_guest, int)
        self.assertIsInstance(P2.price_by_night, int)
        self.assertIsInstance(P2.latitude, float)
        self.assertIsInstance(P2.longitude, float)
        self.assertIsInstance(P2.amenity_ids, list)
