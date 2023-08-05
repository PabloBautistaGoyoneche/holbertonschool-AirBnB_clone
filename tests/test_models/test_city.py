#!/usr/bin/python3
"""We test te class City and all its functions"""
import unittest
import pycodestyle
from models.base_model import BaseModel
from models.city import City
from datetime import datetime


class TestCity(unittest.TestCase):
    """Tests for City class"""

    def test_is_subclass(self):
        """Check if City is a subclass of BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_attr_types(self):
        """Check if attributes of City have correct types"""
        city = City()
        self.assertEqual(type(city.state_id), str)
        self.assertEqual(type(city.name), str)

    def test_attr_defaults(self):
        """Check if attributes of City have correct default values"""
        city = City()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_to_dict(self):
        """Check if to_dict() method returns the correct dictionary"""
        city = City()
        city.state_id = "state-123"
        city.name = "Los Angeles"

        expected_dict = {
            '__class__': 'City',
            'id': city.id,
            'created_at': city.created_at.isoformat(),
            'updated_at': city.updated_at.isoformat(),
            'state_id': 'state-123',
            'name': 'Los Angeles'
        }

        self.assertDictEqual(city.to_dict(), expected_dict)

    def test_from_dict(self):
        """Test from_dict() creates new instance with correct attributes"""
        data = {
            '__class__': 'City',
            'id': 'city-456',
            'created_at': datetime.now().isoformat(),
            'updated_at': datetime.now().isoformat(),
            'state_id': 'state-789',
            'name': 'San Francisco'
        }

        city = City.from_dict(data)

        self.assertIsInstance(city, City)
        self.assertEqual(city.id, 'city-456')
        self.assertEqual(
            city.created_at,
            datetime.strptime(data['created_at'], '%Y-%m-%dT%H:%M:%S.%f')
        )
        self.assertEqual(
            city.updated_at,
            datetime.strptime(data['updated_at'], '%Y-%m-%dT%H:%M:%S.%f')
        )

        self.assertEqual(city.state_id, 'state-789')
        self.assertEqual(city.name, 'San Francisco')

    def test_code_style(self):
        """Check code style using pycodestyle"""
        style = pycodestyle.StyleGuide(quiet=False)
        result = style.check_files(['models/city.py'])
        self.assertEqual(result.total_errors, 0, "Found code style errors")


if __name__ == "__main__":
    unittest.main()
