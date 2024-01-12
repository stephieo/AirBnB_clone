#!/usr/bin/python3
""" Test module for the console"""
import unittest
from models.base_model import BaseModel
from models.user import User
import sys
from console import HBNBCommand
from unittest.mock import patch
from io import StringIO


class TestConsoleBasic(unittest.TestCase):
    """ tests basic functionalities of  the console"""

    @classmethod
    def setUpClass(self):
        self.console0 = HBNBCommand()
    @classmethod
    def tearDownClass(self):
        del self.console0

    def test_emptyline(self):
        """checks that inputing an emptyline or newline does nothing"""
        self.assertEqual(self.console0.onecmd(""), "")
        self.assertEqual(self.console0.onecmd("\n"), "")

    def test_quit_eof(self):
        """checks that quit and EOF exit the console"""
        self.assertEqual(self.console0.onecmd("EOF"), True)
        self.assertTrue(self.console0.onecmd("quit"))

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
        """test create with a missing class"""
        expected = "** class name missing **"

        with patch("sys.stdout", new=StringIO()) as output:
            input_line = "create"
            self.console1.onecmd(input_line)
            self.assertEqual(expected, output.getvalue().strip())
    
    def test_create_wrong_class(self):
        """tests create with wrong class"""
        expected = "** class doesn't exist **"

        with patch("sys.stdout", new=StringIO()) as output:
            input_line = "create jog"
            self.console1.onecmd(input_line)
            self.assertEqual(expected, output.getvalue().strip())

    def test_create_succesful(self):
        """tests successful create command"""

        with patch("sys.stdout", new=StringIO()) as output:
            input_line = "create User"
            self.console1.onecmd(input_line)
            #TODO: add test to check if id returned is valid uuid and if object is saved in storage        


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

    def test_no_id(self):
        """tests show with no id"""
        expected = "** instance id missing **"
        with patch("sys.stdout", new=StringIO()) as output:
            input_line = "show User"
            self.console2.onecmd(input_line)
            self.assertEqual(expected, output.getvalue().strip())

    def test_show_wrong_class_or_id(self):
        """tests show with wrong class or id"""

        expected0 = "** class doesn't exist **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            input_line = "show aUser"
            self.console2.onecmd(input_line)
            self.assertEqual(expected0, output.getvalue().strip())

        expected = "** no instance found **"
        with patch("sys.stdout", new_callable=StringIO) as output:
            input_line = "show User 12345"
            self.console2.onecmd(input_line)
            self.assertEqual(expected, output.getvalue().strip())

    def test_show_valid(self):
        """valid args to show command"""
        u1 = User()
        m1 = BaseModel()

        expected = str(u1)
        with patch("sys.stdout", new=StringIO()) as output:
            input_line = "show User " + u1.id
            self.console2.onecmd(input_line)
            self.assertEqual(expected, output.getvalue().strip())

        expected = str(m1)
        with patch("sys.stdout", new=StringIO()) as output:
            input_line = "show BaseModel " + m1.id
            self.console2.onecmd(input_line)
            self.assertEqual(expected, output.getvalue().strip())

