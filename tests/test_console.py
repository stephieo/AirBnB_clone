#!/usr/bin/python3
""" Test module for the console"""
import unittest
import sys
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO



class TestConsoleMethods(unittest.TestCase):
    """tests each method of the console"""
    pass

class TestCreate(unittest.TestCase):
    """ tests `do_create()`
    Usage:
        create <classname>
    """
    @classmethod
    def setUpClass(self):
        self.console1 = HBNBCommand()
    @classmethod
    def tearDownClass(self):
        del self.console1
    
    def test_create_missing_class(self):
        expected = "** class name missing **"

        with patch("sys.stdout", new=StringIO()) as output:
            input_line = "create"
            self.console1.onecmd(input_line)
            self.assertEqual(expected, output.getvalue().strip())
    
    def test_create_wrong_class(self):
        expected = "** class doesn't exist **"

        with patch("sys.stdout", new=StringIO()) as output:
            input_line = "create jog"
            self.console1.onecmd(input_line)
            self.assertEqual(expected, output.getvalue().strip())

class TestShow(unittest.TestCase):
    """tests do_show()
    Usage:
        show <classname> <id>
    """
    @classmethod
    def setUpClass(self):
        self.console2 = HBNBCommand()
    @classmethod
    def tearDownClass(self):
        del self.console2
    
    def test_show_no_class(self):
        """tests show with no arguments"""
        expected = "** class name missing **"

        with patch("sys.stdout", new=StringIO()) as output:
            input_line = "show"
            self.console2.onecmd(input_line)
            self.assertEqual(expected, output.getvalue().strip())

    def test_show_wrong_class_or_id(self):
        """tests show with wrong class or id"""
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            input_line = "show User"
            self.console2.onecmd(input_line)
            self.assertEqual(expected, output.getvalue().strip())

