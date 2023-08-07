#!/usr/bin/python3
"""We test te class City and all its functions"""
import unittest
from datetime import datetime
from models.city import City


class TestBase(unittest.TestCase):
    """The test class to work in unicode"""

    def testSet(self):
        """Check if you can generate an instance"""
        self.C = City()

    def testExist(self):
        """A test that check if the attributes exists in the class"""
        C1 = City()
        self.assertTrue(hasattr(C1, "id"))
        self.assertTrue(hasattr(C1, "created_at"))
        self.assertTrue(hasattr(C1, "updated_at"))
        self.assertTrue(hasattr(C1, "state_id"))
        self.assertTrue(hasattr(C1, "name"))

    def testUser(self):
        """A test to check if all values are the correct type"""
        C2 = City()
        self.assertIsInstance(C2.id, str)
        self.assertIsInstance(C2.created_at, datetime)
        self.assertIsInstance(C2.updated_at, datetime)
        self.assertIsInstance(C2.state_id, str)
        self.assertIsInstance(C2.name, str)
