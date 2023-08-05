#!/usr/bin/python3
"""We test te class TestFileStorage and all its functions"""
import unittest
import os
import json
from models.base_model import BaseModel
from models.user import User
from models.state import State
from models.city import City
from models.amenity import Amenity
from models.place import Place
from models.review import Review
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        """Set up the test"""
        self.file_path = 'file_test.json'
        self.storage = FileStorage()
        self.storage._FileStorage__file_path = self.file_path

    def tearDown(self):
        """Clean up after each test"""
        try:
            os.remove(self.file_path)
        except FileNotFoundError:
            pass

    def test_save_and_reload(self):
        """Test the save and reload methods"""
        # Create some instances and save them to the file
        user = User()
        user.save()
        state = State()
        state.save()
        city = City()
        city.save()

        # Save the current state of __objects
        original_objects = self.storage._FileStorage__objects.copy()

        # Clear __objects and reload it from the file
        self.storage._FileStorage__objects.clear()
        self.storage.reload()

        # Check that __objects has been restored to its original state
        self.assertDictEqual(
            self.storage._FileStorage__objects,
            original_objects
        )

        # Check that the instances in __objects are of the correct type
        self.assertTrue(isinstance(
            self.storage._FileStorage__objects[
                user.__class__.__name__ + "." + user.id],
            User))
        self.assertTrue(isinstance(
            self.storage._FileStorage__objects[
                state.__class__.__name__ + "." + state.id],
            State))
        self.assertTrue(isinstance(
            self.storage._FileStorage__objects[
                city.__class__.__name__ + "." + city.id],
            City))

    def test_delete(self):
        """Test the delete method"""
        # Create some instances and save them to the file
        user = User()
        user.save()

        # Save the current state of __objects
        original_objects = self.storage._FileStorage__objects.copy()

        # Delete the instance and check that it's removed from __objects
        self.storage.delete(user)
        self.assertNotIn(
            user.__class__.__name__ + "." + user.id,
            self.storage._FileStorage__objects
        )

        # Check that __objects still contains other instances
        self.assertEqual(
            len(self.storage._FileStorage__objects),
            len(original_objects) - 1
        )

    def test_new(self):
        """Test the new method"""
        # Create an instance and call new()
        user = User()
        self.storage.new(user)

        # Check that the instance has been added to __objects
        self.assertIn(
            user.__class__.__name__ + "." + user.id,
            self.storage._FileStorage__objects
        )

    def test_save(self):
        """Test the save method"""
        # Create an instance and save it
        user = User()
        user.save()

        # Read the file and check that the instance is stored in JSON format
        with open(self.file_path, 'r') as file:
            data = json.load(file)
            self.assertIn(user.__class__.__name__ + "." + user.id, data)


if __name__ == "__main__":
    unittest.main()
