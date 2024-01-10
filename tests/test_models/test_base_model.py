#!/usr/bin/python3
"""Test module for `BaseModel` class"""
import unittest
from unittest.mock import patch
from models.base_model import BaseModel
from io import StringIO
import sys

class TestBaseModel(unittest.TestCase):
    """ tests the basic functionalities of the `BaseModel` class"""


    def test_types(self):
        """checks that the type of the object attributes are str and datetime.datetime"""
        mod1 = BaseModel()
        self.assertEqual(type(mod1.id), type(mod1.id))
        self.assertEqual(type(mod1.created_at), type(mod1.created_at))
        self.assertEqual(type(mod1.updated_at), type(mod1.updated_at))

    def test_uniqueness(self):
        """checks that ids are not the same"""
        mod2 = BaseModel()
        mod3 = BaseModel()
        self.assertNotEqual(mod2.id, mod3.id)

class TestBaseModelMethods(unittest.TestCase):
    """ tests the methods of the `BaseModel` classs"""

    @patch('builtins.print')
    def test_str_method(self, mock_output):
        """checks that the output of `str()` matches the requirements"""
        mod1 = BaseModel()
        mod1.name = "first model"
        mod1.number ="30"
        mod_str = f"[{mod1.__class__.__name__}] ({mod1.id}) {mod1.__dict__}"
        output_of_str = str(mod1)
        print(mod1)
        self.assertEqual(output_of_str, mod_str)
        mock_output.assert_called_once_with(mod1)


    def test_to_dict(self):
        """ checks that the output of `to_dict()` matches requirements"""
        mod2 = BaseModel()
        mod2.name = "new model"
        mod2.number = 54
        mod_dict_str = mod2.to_dict()
        self.assertEqual(type(mod_dict_str), dict)
        self.assertEqual(mod_dict_str, mod2.to_dict)

if "__name__" == "__main__":
    unittest.main()