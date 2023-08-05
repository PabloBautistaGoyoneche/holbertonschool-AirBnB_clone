#!/usr/bin/python3
"""We test te class Review and all its functions"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from datetime import datetime


class TestReview(unittest.TestCase):
    """ Test cases for Review class """

    def test_instantiation(self):
        """ Test instantiation """
        review = Review()
        self.assertIsInstance(review, BaseModel)
        self.assertIsInstance(review, Review)
        self.assertEqual(review.place_id, "")
        self.assertEqual(review.user_id, "")
        self.assertEqual(review.text, "")

    def test_to_dict(self):
        """ Test to_dict method """
        review = Review()
        review_dict = review.to_dict()
        self.assertEqual(review_dict['__class__'], 'Review')
        self.assertEqual(type(review_dict['created_at']), str)
        self.assertEqual(type(review_dict['updated_at']), str)

    def test_from_dict(self):
        """ Test from_dict method """
        data = {
            'id': '123',
            'place_id': '456',
            'user_id': '789',
            'text': 'Test review'
        }
        review = Review(**data)
        self.assertEqual(review.id, '123')
        self.assertEqual(review.place_id, '456')
        self.assertEqual(review.user_id, '789')
        self.assertEqual(review.text, 'Test review')

    def test_update_attributes(self):
        """ Test update attributes """
        review = Review()
        self.assertEqual(review.text, "")
        review.text = "New review"
        self.assertEqual(review.text, "New review")

    def test_created_updated_at(self):
        """ Test created_at and updated_at attributes """
        review = Review()
        self.assertIsInstance(review.created_at, datetime)
        self.assertIsInstance(review.updated_at, datetime)
        old_created_at = review.created_at
        old_updated_at = review.updated_at

        # Wait for a moment to simulate time passing
        import time
        time.sleep(1)

        review.save()

        # Make sure updated_at is changed after saving
        self.assertNotEqual(review.updated_at, old_updated_at)

        # Make sure created_at remains the same after saving
        self.assertEqual(review.created_at, old_created_at)

    def test_str_representation(self):
        """ Test __str__ representation """
        review = Review()
        expected_str = "[Review] ({}) {}".format(review.id, review.__dict__)
        self.assertEqual(str(review), expected_str)

    def test_to_dict_with_numeric_attributes(self):
        """ Test of correct storage in the dictionary """
        review = Review()
        review.number_rooms = 3
        review.number_bathrooms = 2
        review.max_guest = 6
        review.price_by_night = 100
        obj_dict = review.to_dict()
        self.assertIn("number_rooms", obj_dict)
        self.assertEqual(obj_dict['number_rooms'], 3)
        self.assertIn("number_bathrooms", obj_dict)
        self.assertEqual(obj_dict['number_bathrooms'], 2)
        self.assertIn("max_guest", obj_dict)
        self.assertEqual(obj_dict['max_guest'], 6)
        self.assertIn("price_by_night", obj_dict)
        self.assertEqual(obj_dict['price_by_night'], 100)


if __name__ == "__main__":
    unittest.main()
