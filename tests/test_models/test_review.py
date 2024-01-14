#!/usr/bin/python3
"""test module for Review class"""
import unittest
from models.review import Review
from models.base_model import BaseModel
from unittest.mock import patch
from io import StringIO
import sys
from datetime import timedelta
from datetime import datetime


class TestReview(unittest.TestCase):
    """ basic type-checking tests of attibutes in  the `Review` class"""

    def test_types(self):
        """confirm types of the custom argumenta"""
        r0a = Review()
        self.assertTrue(type(r0a.place_id), str)
        self.assertTrue(type(r0a.user_id), str)
        self.assertTrue(type(r0a.text), str)

    def test_subclass(self):
        """checks inheritance of `Review` objects"""
        r0 = Review()
        self.assertIsInstance(r0, Review)
        self.assertTrue(issubclass(type(r0), BaseModel))


class TestReviewInstantiation(unittest.TestCase):
    """checks that the instantiation of `Review` objects
    works correctly in various scenarios"""

    def test_init_no_args(self):
        """instantiation test with no arguments"""
        r1 = Review()
        self.assertEqual(isinstance(r1, Review), True)
        self.assertTrue(hasattr(r1, "created_at"))
        self.assertTrue(hasattr(r1, "updated_at"))
        self.assertTrue(hasattr(r1, "id"))
        self.assertAlmostEqual(r1.created_at, r1.updated_at,
                               delta=timedelta(seconds=1))
        self.assertTrue(hasattr(r1, "place_id"))
        self.assertTrue(hasattr(r1, "user_id"))
        self.assertTrue(hasattr(r1, "text"))

    def test_init_custom_args(self):
        """instantiation test of it's own  arguments"""
        r1a = Review()
        self.assertEqual(isinstance(r1a, Review), True)
        self.assertEqual(r1a.place_id, "")
        self.assertEqual(r1a.user_id, "")
        self.assertEqual(r1a.text, "")
        r1a.text = "Great place to stay"
        self.assertEqual(r1a.text, "Great place to stay")

    def test_init_with_args(self):
        """tests instantiation of object with arguments from dictionary"""
        dict1 = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                 'created_at': '2017-09-28T21:03:54.052298',
                 '__class__': 'Review',
                 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302',
                 'name': 'My_First_Model'}
        r2 = Review(**dict1)
        self.assertTrue(hasattr(r2, "created_at"))
        self.assertIsInstance(r2.created_at, datetime)
        self.assertIsInstance(r2.updated_at, datetime)
        self.assertEqual(r2.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")

    def test_init_with_kwargs(self):
        """tests instantiation of object with direct kwargs"""
        r3 = Review(id="78393",
                    created_at="2023-12-14T17:30:54.052298",
                    updated_at="2024-01-02T11:03:54.062721")
        self.assertEqual(type(r3.id), str)
        self.assertEqual(type(r3.created_at), datetime)


class TestReviewMethods(unittest.TestCase):
    """ tests the methods of the `Review` classs"""

    @patch('builtins.print')
    def test_str_method(self, mock_output):
        """checks that the output of `str()` matches the requirements"""
        r4 = Review()
        r4.name = "first model"
        r4.number = "30"
        mod_str = f"[{r4.__class__.__name__}] ({r4.id}) {r4.__dict__}"
        output_of_str = str(r4)
        print(r4)
        self.assertEqual(output_of_str, mod_str)
        mock_output.assert_called_once_with(r4)

    def test_to_dict(self):
        """ checks that the output of `to_dict()` matches requirements"""
        r5 = Review()
        r5.name = "new model"
        r5.number = 54
        mod_dict_str = r5.to_dict()
        self.assertEqual(type(mod_dict_str), dict)
        self.assertIn("Review", r5.to_dict().values())
        self.assertIn("id", r5.to_dict().keys())
        self.assertEqual(type(mod_dict_str['created_at']), str)
        self.assertEqual(type(mod_dict_str['updated_at']), str)

    def test_save(self):
        """checks that the updated_at attribute is updated with save() """
        r6 = Review()
        # print(f"created at: {r6.created_at}")
        # print(f"update 0: {r6.updated_at}")
        self.assertAlmostEqual(r6.created_at, r6.updated_at,
                               delta=timedelta(seconds=1))
        r6.save()
        # print(f"update 1: {r6.updated_at}")
        self.assertNotAlmostEqual(r6.created_at, r6.updated_at,
                                  delta=timedelta(microseconds=10))
        r6.save()
        # print(f"update 2: {r6.updated_at}")
        self.assertNotAlmostEqual(r6.created_at, r6.updated_at,
                                  delta=timedelta(microseconds=1000))
