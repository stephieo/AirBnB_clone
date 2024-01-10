#!/usr/bin/python3
"""The Console"""
import cmd
from models.base_model import BaseModel
from models import storage
from models.engine.file_storage import FileStorage
import json


class HBNBCommand(cmd.Cmd):
    """creates a shell console for our models
    """
    prompt = "(hbnb) "
    __classes = ["BaseModel"]
    __all_objs = storage.all()
    # __all_objs = {keys: values for keys, values in storage.all().items}

    def parse(self, line: str):
        split_line = line.split()
        return split_line

    def do_all(self, line):
        """prints all string representation of all instances based or not
        on the class name
        """
        lines = self.parse(line)
        if (len(lines) == 0):
            objects = [k.__str__() for k in self.__all_objs.values()]
            print(objects)
        else:
            if (lines[0] in self.__classes):
                objects = [k.__str__() for k in self.__all_objs.values()]
                print(objects)
            else:
                print("** class doesn't exist **")

    def do_create(self, line):
        """Creates a new instance of a given Class
        (saves it to the JSON file and prints the id)"""
        lines = self.parse(line)
        if (len(lines) == 0):
            print("** class name missing **")
        elif (lines[0] not in self.__classes):
            """** class doesn't exist **"""
        else:
            obj = BaseModel()
            print(obj.id)
            obj.save()
            self.__all_objs = storage.all()

    def do_destroy(self, line):
        """Deletes an instance based on the class name and id
        (save the change into the JSON file)
        """
        lines = self.parse(line)
        if (len(lines) == 0):
            print("** class name missing **")
        elif (lines[0] not in self.__classes):
            print("** class doesn't exist **")
        elif (len(lines) == 1):
            print("** instance id missing **")
        else:
            cls_n_id = lines[0] + "." + lines[1]
            if cls_n_id not in self.__all_objs.keys():
                print("** no instance found **")
            else:
                del self.__all_objs[cls_n_id]
            self.__all_objs = storage.all()

    def do_EOF(self, line):
        """Quit command to exit the program"""
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_show(self, line):
        """prints the string representation of an instance
        based on class name and id
        """
        lines = self.parse(line)
        if (len(lines) == 0):
            print("** class name missing **")
        elif (lines[0] not in self.__classes):
            print("** class doesn't exist **")
        elif (len(lines) == 1):
            print("** instance id missing **")
        else:
            cls_n_id = lines[0] + "." + lines[1]
            if cls_n_id not in self.__all_objs.keys():
                print("** no instance found **")
            else:
                print(self.__all_objs[cls_n_id])

    def do_update(self, line):
        """updates an instance based on the class name and id by adding
        or updating attribute (save the change into the JSON file)
        """
        lines = self.parse(line)
        if (len(lines) == 0):
            print("** class name missing **")
        elif (lines[0] not in self.__classes):
            print("** class doesn't exist **")
        elif (len(lines) == 1):
            print("** instance id missing **")
        else:
            cls_n_id = lines[0] + "." + lines[1]
            if cls_n_id not in self.__all_objs.keys():
                print("** no instance found **")
            elif (len(lines) == 2):
                print("** attribute name missing **")
            elif (len(lines) == 3):
                print("** value missing **")
            else:
                obj = self.__all_objs[cls_n_id]
                setattr(obj, lines[2], eval(lines[3]))
                eval(lines[0]).save(obj)
                # self.__all_objs = storage.all()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
