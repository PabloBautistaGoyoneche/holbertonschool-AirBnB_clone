#!/usr/bin/python3
"""We test te class State and all its functions"""
import unittest
from datetime import datetime
from models.state import State


class TestBase(unittest.TestCase):
    """The test class to work in unicode"""

    def testSet(self):
        """Check if you can generate an instance"""
        self.S = State()

    def testExist(self):
        """A test that check if the attributes exists in the class"""
        S1 = State()
        self.assertTrue(hasattr(S1, "id"))
        self.assertTrue(hasattr(S1, "created_at"))
        self.assertTrue(hasattr(S1, "updated_at"))
        self.assertTrue(hasattr(S1, "name"))

    def testUser(self):
        """A test to check if all values are the correct type"""
        S2 = State()
        self.assertIsInstance(S2.id, str)
        self.assertIsInstance(S2.created_at, datetime)
        self.assertIsInstance(S2.updated_at, datetime)
        self.assertIsInstance(S2.name, str)
