#!/usr/bin/python3
""" Test module for 'FileStorage' class"""
import unittest
import models
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage

class TestFileStorageMethods(unittest.TestCase):
    """tests all methods of the `FileStorage` class"""

    def SetUp(self):
        """setup for this testcase"""

    def test_new(self):
        """checks that new() updates the __objects dictionary with new instances"""
        f1 = BaseModel()
        self.assertIn(f1.__class__.__name__ + "." + f1.id, models.storage._FileStorage__objects)

    def test_all(self):
        """checks that the correct object record is returned"""
        all_objs = models.storage.all()
        print(all_objs)
        self.assertEqual(type(all_objs), dict)

    def test_save(self):
        """checks serialization process of instances in __objects"""
        

    def test_reload(self):
        """checks deserialization process of objects"""
        pass