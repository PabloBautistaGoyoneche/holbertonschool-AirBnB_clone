#!/usr/bin/python3
"""We test te class User and all its functions"""
import unittest
from models.user import User
import json
import os
from datetime import datetime


class TestUser(unittest.TestCase):
    def setUp(self):
        self.user = User()

    def tearDown(self):
        try:
            os.remove("file.json")
        except FileNotFoundError:
            pass

    def test_instance(self):
        self.assertIsInstance(self.user, User)

    def test_attributes(self):
        self.assertTrue(hasattr(self.user, "email"))
        self.assertTrue(hasattr(self.user, "password"))
        self.assertTrue(hasattr(self.user, "first_name"))
        self.assertTrue(hasattr(self.user, "last_name"))

    def test_attributes_defaults(self):
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_to_dict(self):
        user_dict = self.user.to_dict()
        self.assertEqual(type(user_dict), dict)
        self.assertEqual(user_dict["__class__"], "User")
        self.assertEqual(type(user_dict["created_at"]), str)
        self.assertEqual(type(user_dict["updated_at"]), str)

    def test_to_dict_created_at(self):
        user_dict = self.user.to_dict()
        created_at = datetime.strptime(user_dict["created_at"],
                                       "%Y-%m-%dT%H:%M:%S.%f")
        self.assertEqual(created_at, self.user.created_at)

    def test_save(self):
        self.user.save()
        with open("file.json", "r") as file:
            data = json.load(file)
            user_key = "User." + self.user.id
            self.assertTrue(user_key in data)
            user_dict = data[user_key]
            self.assertEqual(user_dict["email"], self.user.email)
            self.assertEqual(user_dict["password"], self.user.password)
            self.assertEqual(user_dict["first_name"], self.user.first_name)
            self.assertEqual(user_dict["last_name"], self.user.last_name)
            created_at = datetime.strptime(user_dict["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f")
            self.assertEqual(created_at, self.user.created_at)

    def test_reload(self):
        self.user.save()
        user_id = self.user.id
        del self.user
        new_user = User()
        self.assertEqual(new_user.email, "")
        self.assertEqual(new_user.password, "")
        self.assertEqual(new_user.first_name, "")
        self.assertEqual(new_user.last_name, "")
        self.assertEqual(new_user.id, user_id)
        with open("file.json", "r") as file:
            data = json.load(file)
            user_key = "User." + user_id
            self.assertTrue(user_key in data)
            user_dict = data[user_key]
            self.assertEqual(user_dict["email"], new_user.email)
            self.assertEqual(user_dict["password"], new_user.password)
            self.assertEqual(user_dict["first_name"], new_user.first_name)
            self.assertEqual(user_dict["last_name"], new_user.last_name)
            created_at = datetime.strptime(user_dict["created_at"],
                                           "%Y-%m-%dT%H:%M:%S.%f")
            self.assertEqual(created_at, new_user.created_at)

    def test_to_dict_with_first_name(self):
        user = User()
        user.first_name = "John"
        obj_dict = user.to_dict()
        self.assertIn("first_name", obj_dict)
        self.assertEqual(obj_dict['first_name'], "John")


if __name__ == "__main__":
    unittest.main()
