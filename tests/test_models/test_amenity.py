#!/usr/bin/python3
"""We test te class Amenity and all its functions"""
import unittest
from datetime import datetime
from models.amenity import Amenity


class TestBase(unittest.TestCase):
    """The test class to work in unicode"""

    def testSet(self):
        """Check if you can generate an instance"""
        self.C = Amenity()

    def testExist(self):
        """A test that check if the attributes exists in the class"""
        A1 = Amenity()
        self.assertTrue(hasattr(A1, "id"))
        self.assertTrue(hasattr(A1, "created_at"))
        self.assertTrue(hasattr(A1, "updated_at"))
        self.assertTrue(hasattr(A1, "name"))

    def testUser(self):
        """A test to check if all values are the correct type"""
        A2 = Amenity()
        self.assertIsInstance(A2.id, str)
        self.assertIsInstance(A2.created_at, datetime)
        self.assertIsInstance(A2.updated_at, datetime)
        self.assertIsInstance(A2.name, str)
