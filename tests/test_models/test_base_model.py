#!/usr/bin/python3
""" Unit tests for BaseModel """
import unittest
from models.base_model import BaseModel
from datetime import datetime
from time import sleep


class TestBaseModel(unittest.TestCase):
    """Unit tests for BaseModel"""

    def test_instantiate(self):
        """Happy pass instantiate"""
        self.assertEqual(BaseModel, type(BaseModel()))

    def test_id(self):
        """Happy pass public id string format"""
        self.assertEqual(str, type(BaseModel().id))

    def test_created_at(self):
        """Happy pass created at datetime"""
        self.assertEqual(datetime, type(BaseModel().created_at))

    def test_updated_at(self):
        """Happy pass updated at datetime"""
        self.assertEqual(datetime, type(BaseModel().updated_at))

    def test_uid(self):
        """UID created at each instantiation"""
        base1 = BaseModel()
        base2 = BaseModel()
        self.assertNotEqual(base1.id, base2.id)

    def test_instantiate_attrs(self):
        """Single instantiate and check attributes"""
        base1 = BaseModel()
        self.assertEqual(type(base1.id), str)
        self.assertEqual(type(base1.created_at), datetime)
        self.assertEqual(type(base1.updated_at), datetime)

    def test_instantiate_kwargs(self):
        """Single instantiate with kwargs"""
        dt = datetime.today()
        base1 = BaseModel(
            id="123", created_at=dt.isoformat(), updated_at=dt.isoformat()
        )
        self.assertEqual(base1.id, "123")
        self.assertEqual(base1.created_at, dt)
        self.assertEqual(base1.updated_at, dt)

    def test_str(self):
        """___str__ method is string"""
        base1 = BaseModel()
        self.assertEqual(type(str(base1)), str)

    def test_instantiate_arg(self):
        """Invalid arg when instantiating"""
        with self.assertRaises(TypeError) as e:
            hello = "hello"
            b1 = BaseModel(hello)
        self.assertEqual(
            str(e.exception), "name 'hello' is not defined"
        )

    def test_save(self):
        """save method"""
        base1 = BaseModel()
        sleep(2)
        update = base1.updated_at
        base1.save()
        self.assertNotEqual(update, base1.updated_at)

    def test_to_dict(self):
        """Happy pass to_dict method"""
        base1 = BaseModel()
        self.assertTrue(dict, type(base1.to_dict))

    def test_to_dict_add_attr(self):
        """Add attribute to dict"""
        base1 = BaseModel()
        base1.city = "LA"
        base1.state = "California"
        self.assertIn("city", base1.to_dict())
        self.assertIn("state", base1.to_dict())

    def test_to_dict_wrong_arg(self):
        """Add an undefined arg"""
        base1 = BaseModel()
        with self.assertRaises(TypeError):
            hello = "hello"
            base1.to_dict(hello)

    def test_from_dict(self):
        # Check if from_dict() method creates a new instance with
        # the correct attributes
        data = {
            "__class__": "BaseModel",
            "id": "123",
            "created_at": "2022-01-01T12:00:00.000000",
            "updated_at": "2022-01-01T12:00:00.000000",
            "custom_attribute": "custom_value",
        }
        base1 = BaseModel.from_dict(data)
        self.assertIsInstance(base1, BaseModel)
        self.assertEqual(base1.id, "123")
        self.assertEqual(
            base1.created_at, datetime(2022, 1, 1, 12, 0, 0)
        )
        self.assertEqual(
            base1.updated_at, datetime(2022, 1, 1, 12, 0, 0)
        )
        self.assertNotIn("custom_attribute", base1.__dict__)

    def test_delete(self):
        """Test delete method"""
        base1 = BaseModel()
        self.assertIn(
            base1.__class__.__name__ + "." + base1.id,
            base1._FileStorage__objects,
        )
        base1.delete()
        self.assertNotIn(
            base1.__class__.__name__ + "." + base1.id,
            base1._FileStorage__objects,
        )

    def test_delete_with_arg(self):
        """Test delete method with an instance argument"""
        base1 = BaseModel()
        self.assertIn(
            base1.__class__.__name__ + "." + base1.id,
            base1._FileStorage__objects,
        )
        base1.delete(base1)
        self.assertNotIn(
            base1.__class__.__name__ + "." + base1.id,
            base1._FileStorage__objects,
        )

    def test_to_dict_with_keys(self):
        """Test to_dict method contains correct keys"""
        base1 = BaseModel()
        dic = base1.to_dict()
        self.assertIn("__class__", dic)
        self.assertIn("id", dic)
        self.assertIn("created_at", dic)
        self.assertIn("updated_at", dic)

    def test_reload(self):
        """Test reload method"""
        base1 = BaseModel()
        base2 = BaseModel()
        base2.delete()
        self.assertNotEqual(
            base1.updated_at, base2.updated_at
        )
        base1.reload()
        self.assertEqual(
            base1.updated_at, base2.updated_at
        )

    def test_reload_with_arg(self):
        """Test reload method with an instance argument"""
        base1 = BaseModel()
        base2 = BaseModel()
        base2.delete()
        self.assertNotEqual(
            base1.updated_at, base2.updated_at
        )
        base1.reload(base1)
        self.assertEqual(
            base1.updated_at, base2.updated_at
        )

    def test_reload_with_arg_invalid_instance(self):
        """Test reload method with an invalid instance argument"""
        base1 = BaseModel()
        with self.assertRaises(AttributeError):
            base1.reload("invalid_instance")

    def test_reload_without_file(self):
        """Test reload method without file"""
        base1 = BaseModel()
        base1.delete()
        base1.reload()
        self.assertNotIn(
            base1.__class__.__name__ + "." + base1.id,
            base1._FileStorage__objects,
        )

    def test_reload_with_arg_without_file(self):
        """Test reload method with an instance argument without file"""
        base1 = BaseModel()
        base1.delete()
        base1.reload(base1)
        self.assertNotIn(
            base1.__class__.__name__ + "." + base1.id,
            base1._FileStorage__objects,
        )


if __name__ == "__main__":
    unittest.main()
