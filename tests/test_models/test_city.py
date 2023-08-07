#!/usr/bin/python3
"""We test te class City and all its functions"""
import unittest
from models.city import City
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestCity(unittest.TestCase):
    """Unit tests for City"""

    def setUp(self):
        self.city1 = City()
        self.city2 = City(name="New York", state_id="12345")

    def test_instantiate(self):
        """Happy pass instantiate"""
        self.assertIsInstance(self.city1, City)
        self.assertIsInstance(self.city2, City)

    def test_inherit_from_base_model(self):
        """City inherits from BaseModel"""
        self.assertTrue(issubclass(City, BaseModel))

    def test_id(self):
        """Happy pass public id string format"""
        self.assertEqual(str, type(self.city1.id))
        self.assertEqual(str, type(self.city2.id))

    def test_created_at(self):
        """Happy pass created at datetime"""
        self.assertEqual(datetime, type(self.city1.created_at))
        self.assertEqual(datetime, type(self.city2.created_at))

    def test_updated_at(self):
        """Happy pass updated at datetime"""
        self.assertEqual(datetime, type(self.city1.updated_at))
        self.assertEqual(datetime, type(self.city2.updated_at))

    def test_uid(self):
        """UID created at each instantiation"""
        self.assertNotEqual(self.city1.id, self.city2.id)

    def test_instantiate_attrs(self):
        """Single instantiate and check attributes"""
        self.assertEqual(type(self.city1.id), str)
        self.assertEqual(type(self.city1.created_at), datetime)
        self.assertEqual(type(self.city1.updated_at), datetime)

    def test_str(self):
        """___str__ method is string"""
        self.assertEqual(type(str(self.city1)), str)
        self.assertEqual(type(str(self.city2)), str)

    def test_instantiate_arg(self):
        """Invalid arg when instantiating"""
        with self.assertRaises(NameError) as e:
            hello = "hello"
            City(hello)
        self.assertEqual(
            str(e.exception), "name 'hello' is not defined"
        )

    def test_save(self):
        """save method"""
        update1 = self.city1.updated_at
        update2 = self.city2.updated_at
        sleep(2)
        self.city1.save()
        self.city2.save()
        self.assertNotEqual(update1, self.city1.updated_at)
        self.assertNotEqual(update2, self.city2.updated_at)

    def test_to_dict(self):
        """Happy pass to_dict method"""
        dic1 = self.city1.to_dict()
        dic2 = self.city2.to_dict()
        self.assertIsInstance(dic1, dict)
        self.assertIsInstance(dic2, dict)
        self.assertEqual("__class__" in dic1, True)
        self.assertEqual("__class__" in dic2, True)
        self.assertEqual("id" in dic1, True)
        self.assertEqual("id" in dic2, True)
        self.assertEqual("created_at" in dic1, True)
        self.assertEqual("created_at" in dic2, True)
        self.assertEqual("updated_at" in dic1, True)
        self.assertEqual("updated_at" in dic2, True)

    def test_to_dict_add_attr(self):
        """Add attribute to dict"""
        self.city1.state_id = "123"
        self.city1.name = "Los Angeles"
        dic = self.city1.to_dict()
        self.assertIn("state_id", dic)
        self.assertIn("name", dic)
        self.assertEqual(dic["state_id"], "123")
        self.assertEqual(dic["name"], "Los Angeles")

    def test_from_dict(self):
        # Check if from_dict() method creates a new instance
        # with the correct attributes
        data1 = {
            "__class__": "City",
            "id": "123",
            "created_at": "2022-01-01T12:00:00.000000",
            "updated_at": "2022-01-01T12:00:00.000000",
            "custom_attribute": "custom_value",
        }
        data2 = {
            "__class__": "City",
            "id": "456",
            "created_at": "2023-02-02T14:30:00.000000",
            "updated_at": "2023-02-02T14:30:00.000000",
            "state_id": "789",
            "name": "Chicago",
        }
        city1 = City.from_dict(data1)
        city2 = City.from_dict(data2)
        self.assertIsInstance(city1, City)
        self.assertIsInstance(city2, City)
        self.assertEqual(city1.id, "123")
        self.assertEqual(city2.id, "456")
        self.assertEqual(
            city1.created_at, datetime(2022, 1, 1, 12, 0, 0)
        )
        self.assertEqual(
            city2.created_at, datetime(2023, 2, 2, 14, 30, 0)
        )
        self.assertEqual(
            city1.updated_at, datetime(2022, 1, 1, 12, 0, 0)
        )
        self.assertEqual(
            city2.updated_at, datetime(2023, 2, 2, 14, 30, 0)
        )
        self.assertNotIn("custom_attribute", city1.__dict__)
        self.assertIn("state_id", city2.__dict__)
        self.assertIn("name", city2.__dict__)

    def test_delete(self):
        """Test delete method"""
        self.assertIn(
            self.city1.__class__.__name__ + "." + self.city1.id,
            self.city1._FileStorage__objects,
        )
        self.assertIn(
            self.city2.__class__.__name__ + "." + self.city2.id,
            self.city2._FileStorage__objects,
        )
        self.city1.delete()
        self.city2.delete()
        self.assertNotIn(
            self.city1.__class__.__name__ + "." + self.city1.id,
            self.city1._FileStorage__objects,
        )
        self.assertNotIn(
            self.city2.__class__.__name__ + "." + self.city2.id,
            self.city2._FileStorage__objects,
        )

    def test_delete_with_arg(self):
        """Test delete method with an instance argument"""
        self.assertIn(
            self.city1.__class__.__name__ + "." + self.city1.id,
            self.city1._FileStorage__objects,
        )
        self.assertIn(
            self.city2.__class__.__name__ + "." + self.city2.id,
            self.city2._FileStorage__objects,
        )
        self.city1.delete(self.city1)
        self.city2.delete(self.city2)
        self.assertNotIn(
            self.city1.__class__.__name__ + "." + self.city1.id,
            self.city1._FileStorage__objects,
        )
        self.assertNotIn(
            self.city2.__class__.__name__ + "." + self.city2.id,
            self.city2._FileStorage__objects,
        )


if __name__ == "__main__":
    unittest.main()
