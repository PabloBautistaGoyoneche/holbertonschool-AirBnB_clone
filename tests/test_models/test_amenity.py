#!/usr/bin/python3
"""We test te class Amenity and all its functions"""
import unittest

from models.amenity import Amenity
from datetime import datetime
from time import sleep


class TestAmenity(unittest.TestCase):
    """Unit tests for Amenity"""

    def test_instantiate(self):
        """Happy pass instantiate"""
        self.assertEqual(Amenity, type(Amenity()))

    def test_id(self):
        """Happy pass public id string format"""
        self.assertEqual(str, type(Amenity().id))

    def test_created_at(self):
        """Happy pass created at datetime"""
        self.assertEqual(datetime, type(Amenity().created_at))

    def test_updated_at(self):
        """Happy pass updated at datetime"""
        self.assertEqual(datetime, type(Amenity().updated_at))

    def test_uid(self):
        """UID created at each instantiation"""
        amenity1 = Amenity()
        amenity2 = Amenity()
        self.assertNotEqual(amenity1.id, amenity2.id)

    def test_instantiate_attrs(self):
        """Single instantiate and check attributes"""
        amenity1 = Amenity()
        self.assertEqual(type(amenity1.id), str)
        self.assertEqual(type(amenity1.created_at), datetime)
        self.assertEqual(type(amenity1.updated_at), datetime)

    def test_instantiate_kwargs(self):
        """Single instantiate with kwargs"""
        dt = datetime.today()
        amenity1 = Amenity(
            id="123", created_at=dt.isoformat(), updated_at=dt.isoformat()
        )
        self.assertEqual(amenity1.id, "123")
        self.assertEqual(amenity1.created_at, dt)
        self.assertEqual(amenity1.updated_at, dt)

    def test_str(self):
        """___str__ method is string"""
        amenity1 = Amenity()
        self.assertEqual(type(str(amenity1)), str)

    def test_instantiate_arg(self):
        """Invalid arg when instantiating"""
        with self.assertRaises(TypeError) as e:
            hello = "hello"
            a1 = Amenity(hello)
        self.assertEqual(
            str(e.exception), "name 'hello' is not defined"
        )

    def test_save(self):
        """save method"""
        amenity1 = Amenity()
        sleep(2)
        update = amenity1.updated_at
        amenity1.save()
        self.assertNotEqual(update, amenity1.updated_at)

    def test_to_dict(self):
        """Happy pass to_dict method"""
        amenity1 = Amenity()
        self.assertTrue(dict, type(amenity1.to_dict))

    def test_to_dict_add_attr(self):
        """Add attribute to dict"""
        amenity1 = Amenity()
        amenity1.city = "LA"
        amenity1.state = "California"
        self.assertIn("city", amenity1.to_dict())
        self.assertIn("state", amenity1.to_dict())

    def test_to_dict_wrong_arg(self):
        """Add an undefined arg"""
        amenity1 = Amenity()
        with self.assertRaises(TypeError):
            hello = "hello"
            amenity1.to_dict(hello)

    def test_delete(self):
        """Test delete method"""
        amenity1 = Amenity()
        self.assertIn(
            amenity1.__class__.__name__ + "." + amenity1.id,
            amenity1._FileStorage__objects,
        )
        amenity1.delete()
        self.assertNotIn(
            amenity1.__class__.__name__ + "." + amenity1.id,
            amenity1._FileStorage__objects,
        )

    def test_to_dict_with_keys(self):
        """Test to_dict method contains correct keys"""
        amenity1 = Amenity()
        dic = amenity1.to_dict()
        self.assertIn("__class__", dic)
        self.assertIn("id", dic)
        self.assertIn("created_at", dic)
        self.assertIn("updated_at", dic)

    def test_reload_with_arg(self):
        """Test reload method with an instance argument"""
        amenity1 = Amenity()
        amenity2 = Amenity()
        amenity2.delete()
        self.assertNotEqual(
            amenity1.updated_at, amenity2.updated_at
        )
        amenity1.reload(amenity1)
        self.assertEqual(
            amenity1.updated_at, amenity2.updated_at
        )

    def test_reload_with_arg_invalid_instance(self):
        """Test reload method with an invalid instance argument"""
        amenity1 = Amenity()
        with self.assertRaises(AttributeError):
            amenity1.reload("invalid_instance")

    def test_reload_without_file(self):
        """Test reload method without file"""
        amenity1 = Amenity()
        amenity1.delete()
        amenity1.reload()
        self.assertNotIn(
            amenity1.__class__.__name__ + "." + amenity1.id,
            amenity1._FileStorage__objects,
        )

    def test_reload_with_arg_without_file(self):
        """Test reload method with an instance argument without file"""
        amenity1 = Amenity()
        amenity1.delete()
        amenity1.reload(amenity1)
        self.assertNotIn(
            amenity1.__class__.__name__ + "." + amenity1.id,
            amenity1._FileStorage__objects,
        )


if __name__ == "__main__":
    unittest.main()
