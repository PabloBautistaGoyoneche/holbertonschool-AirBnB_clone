#!/usr/bin/python3
import unittest
from models.amenity import Amenity
from datetime import datetime


class TestAmenity(unittest.TestCase):
    """ Unit tests for Amenity """

    def test_instantiate(self):
        """ Happy pass instantiate"""
        self.assertEqual(Amenity, type(Amenity()))

    def test_name_attribute(self):
        """ name attribute is a string """
        self.assertEqual(str, type(Amenity().name))

    def test_created_at(self):
        """ Happy pass created at datetime """
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at(self):
        """ Happy pass updated at datetime """
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_str(self):
        """ ___str__ method is string """
        amenity1 = Amenity()
        self.assertEqual(type(str(amenity1)), str)

    def test_instantiate_args(self):
        """ invalid arg when instantiating """
        with self.assertRaises(TypeError) as e:
            amenity1 = Amenity(123)
        self.assertEqual(str(e.exception), (
            "__init__() takes 1 positional argument but 2 were given"))


if __name__ == "__main__":
    unittest.main()
