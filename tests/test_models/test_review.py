#!/usr/bin/python3
"""We test te class Review and all its functions"""
import unittest
from datetime import datetime
from models.review import Review


class TestBase(unittest.TestCase):
    """The test class to work in unicode"""

    def testSet(self):
        """Check if you can generate an instance"""
        self.R = Review()

    def testExist(self):
        """A test that check if the attributes exists in the class"""
        R1 = Review()
        self.assertTrue(hasattr(R1, "id"))
        self.assertTrue(hasattr(R1, "created_at"))
        self.assertTrue(hasattr(R1, "updated_at"))
        self.assertTrue(hasattr(R1, "place_id"))
        self.assertTrue(hasattr(R1, "user_id"))
        self.assertTrue(hasattr(R1, "text"))

    def testUser(self):
        """A test to check if all values are the correct type"""
        R2 = Review()
        self.assertIsInstance(R2.id, str)
        self.assertIsInstance(R2.created_at, datetime)
        self.assertIsInstance(R2.updated_at, datetime)
        self.assertIsInstance(R2.place_id, str)
        self.assertIsInstance(R2.user_id, str)
        self.assertIsInstance(R2.text, str)
