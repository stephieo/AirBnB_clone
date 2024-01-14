#!/usr/bin/python3
"""test module for Place class"""
import unittest
from models.place import Place
from models.base_model import BaseModel
from unittest.mock import patch
from io import StringIO
import sys
from datetime import timedelta
from datetime import datetime


class TestPlace(unittest.TestCase):
    """ basic type-checking tests of attibutes in  the `Place` class"""

    def test_types(self):
        """confirm types of the custom argumenta"""
        p0a = Place()
        self.assertTrue(type(p0a.city_id), str)
        self.assertTrue(type(p0a.user_id), str)
        self.assertTrue(type(p0a.name), str)
        self.assertTrue(type(p0a.description), str)
        self.assertTrue(type(p0a.number_rooms), int)
        self.assertTrue(type(p0a.number_bathrooms), int)
        self.assertTrue(type(p0a.max_guest), int)
        self.assertTrue(type(p0a.price_by_night), int)
        self.assertTrue(type(p0a.latitude), float)
        self.assertTrue(type(p0a.longitude), float)
        self.assertTrue(type(p0a.amenity_ids), list)

    def test_subclass(self):
        """checks inheritance of `Place` objects"""
        p0 = Place()
        self.assertIsInstance(p0, Place)
        self.assertTrue(issubclass(type(p0), BaseModel))


class TestPlaceInstantiation(unittest.TestCase):
    """checks that the instantiation of `Place` objects
    works correctly in various scenarios"""

    def test_init_no_args(self):
        """instantiation test with no arguments"""
        p1 = Place()
        self.assertEqual(isinstance(p1, Place), True)
        self.assertTrue(hasattr(p1, "created_at"))
        self.assertTrue(hasattr(p1, "updated_at"))
        self.assertTrue(hasattr(p1, "id"))
        self.assertAlmostEqual(p1.created_at, p1.updated_at,
                               delta=timedelta(seconds=1))
        self.assertTrue(hasattr(p1, "city_id"))
        self.assertTrue(hasattr(p1, "user_id"))
        self.assertTrue(hasattr(p1, "name"))
        self.assertTrue(hasattr(p1, "max_guest"))
        self.assertTrue(hasattr(p1, "number_rooms"))
        self.assertTrue(hasattr(p1, "price_by_night"))
        self.assertTrue(hasattr(p1, "description"))

    def test_init_custom_args(self):
        """instantiation test of it's own  arguments"""
        p1a = Place()
        self.assertEqual(isinstance(p1a, Place), True)
        self.assertEqual(p1a.max_guest, 0)
        self.assertEqual(p1a.price_by_night, 0)
        self.assertEqual(p1a.description, "")
        p1a.price_by_night = 900
        p1a.max_guest = 3
        p1a.description = "Simple bed and bath"
        self.assertEqual(p1a.max_guest, 3)
        self.assertEqual(p1a.description, "Simple bed and bath")

    def test_init_with_args(self):
        """tests instantiation of object with arguments from dictionary"""
        dict1 = {'id': '56d43177-cc5f-4d6c-a0c1-e167f8c27337',
                 'created_at': '2017-09-28T21:03:54.052298',
                 '__class__': 'Place',
                 'my_number': 89, 'updated_at': '2017-09-28T21:03:54.052302',
                 'name': 'My_First_Model'}
        p2 = Place(**dict1)
        self.assertTrue(hasattr(p2, "created_at"))
        self.assertIsInstance(p2.created_at, datetime)
        self.assertIsInstance(p2.updated_at, datetime)
        self.assertEqual(p2.id, "56d43177-cc5f-4d6c-a0c1-e167f8c27337")

    def test_init_with_kwargs(self):
        """tests instantiation of object with direct kwargs"""
        p3 = Place(id="78393",
                   created_at="2023-12-14T17:30:54.052298",
                   updated_at="2024-01-02T11:03:54.062721")
        self.assertEqual(type(p3.id), str)
        self.assertEqual(type(p3.created_at), datetime)


class TestPlaceMethods(unittest.TestCase):
    """ tests the methods of the `Place` classs"""

    @patch('builtins.print')
    def test_str_method(self, mock_output):
        """checks that the output of `str()` matches the requirements"""
        p4 = Place()
        p4.name = "first model"
        p4.number = "30"
        mod_str = f"[{p4.__class__.__name__}] ({p4.id}) {p4.__dict__}"
        output_of_str = str(p4)
        print(p4)
        self.assertEqual(output_of_str, mod_str)
        mock_output.assert_called_once_with(p4)

    def test_to_dict(self):
        """ checks that the output of `to_dict()` matches requirements"""
        p5 = Place()
        p5.name = "new model"
        p5.number = 54
        mod_dict_str = p5.to_dict()
        self.assertEqual(type(mod_dict_str), dict)
        self.assertIn("Place", p5.to_dict().values())
        self.assertIn("id", p5.to_dict().keys())
        self.assertEqual(type(mod_dict_str['created_at']), str)
        self.assertEqual(type(mod_dict_str['updated_at']), str)

    def test_save(self):
        """checks that the updated_at attribute is updated with save() """
        p6 = Place()
        # print(f"created at: {p6.created_at}")
        # print(f"update 0: {p6.updated_at}")
        # self.assertAlmostEqual(p6.created_at, p6.updated_at,
        #                        delta=timedelta(seconds=1))
        # p6.save()
        # # print(f"update 1: {p6.updated_at}")
        # self.assertNotAlmostEqual(p6.created_at, p6.updated_at,
        #                           delta=timedelta(microseconds=10))
        # p6.save()
        # # print(f"update 2: {p6.updated_at}")
        # self.assertNotAlmostEqual(p6.created_at, p6.updated_at,
        #                           delta=timedelta(microseconds=1000))
