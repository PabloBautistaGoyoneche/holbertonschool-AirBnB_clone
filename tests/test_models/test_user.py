#!/usr/bin/python3
"""We test te class User and all its functions"""
import unittest
from datetime import datetime
from models.user import User


class TestBase(unittest.TestCase):
    """The test class to work in unicode"""

    def testSet(self):
        """Check if you can generate an instance"""
        self.U = User()

    def testExist(self):
        """A test that check if the attributes exists in the class"""
        U1 = User()
        self.assertTrue(hasattr(U1, "id"))
        self.assertTrue(hasattr(U1, "created_at"))
        self.assertTrue(hasattr(U1, "updated_at"))
        self.assertTrue(hasattr(U1, "email"))
        self.assertTrue(hasattr(U1, "password"))
        self.assertTrue(hasattr(U1, "first_name"))
        self.assertTrue(hasattr(U1, "last_name"))

    def testUser(self):
        """A test to check if all values are the correct type"""
        U2 = User()
        self.assertIsInstance(U2.id, str)
        self.assertIsInstance(U2.created_at, datetime)
        self.assertIsInstance(U2.updated_at, datetime)
        self.assertIsInstance(U2.email, str)
        self.assertIsInstance(U2.password, str)
        self.assertIsInstance(U2.first_name, str)
        self.assertIsInstance(U2.last_name, str)
