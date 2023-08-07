#!/usr/bin/python3
"""We test te class Base Model and all its functions"""
import unittest
from datetime import datetime
from models.base_model import BaseModel


class TestBase(unittest.TestCase):
    """The test class to work in unicode"""

    def testSetUp(self):
        """Check if you can generate an instance"""
        self.B = BaseModel()

    def testExist(self):
        """A test that check if the attributes exists in the class"""
        B5 = BaseModel()
        self.assertTrue(hasattr(B5, "id"))
        self.assertTrue(hasattr(B5, "created_at"))
        self.assertTrue(hasattr(B5, "updated_at"))

    def testBase(self):
        """A test to check if all values are the correct type"""
        B1 = BaseModel()
        self.assertIsInstance(B1.id, str)
        self.assertIsInstance(B1.created_at, datetime)
        self.assertIsInstance(B1.updated_at, datetime)

    def testSave(self):
        """a test to check if the save function changes the
        value of update_at"""
        B2 = BaseModel()
        prevUp = B2.updated_at
        B2.save()
        self.assertNotEquals(prevUp, B2.updated_at)

    def testToDict(self):
        """a test that check if to dict function work correctly"""
        B3 = BaseModel()
        keys = ['id', 'created_at', 'updated_at', '__class__']
        b3_dict = B3.to_dict()
        for key in keys:
            self.assertIn(key, b3_dict)

    def test_to_dict_returns(self):
        """a test to check if a dictionary is returned"""
        B3 = BaseModel()
        instance_dict = B3.to_dict()

    def test_to_dict_attributes(self):
        """chcckes if args in dictionary are expected"""
        B3 = BaseModel()
        instances_dicts = B3.to_dict()
        self.assertIn('id', instances_dicts)
        self.assertIn('created_at', instances_dicts)
        self.assertIn('updated_at', instances_dicts)

    def testTodictFormat(self):
        """a test for the isoformat values"""
        B4 = BaseModel()
        b4_dict = B4.to_dict()
        created_at = datetime.fromisoformat(b4_dict['created_at'])
        updated_at = datetime.fromisoformat(b4_dict['updated_at'])
        self.assertIsInstance(created_at, datetime)
        self.assertIsInstance(updated_at, datetime)

    def testStr(self):
        B6 = BaseModel
        pr = str(B6)
        self.assertIn(self.__class__.__name__, pr)
        self.assertIn(self.__class__.id)


if __name__ == '__main__':
    unittest.main()
