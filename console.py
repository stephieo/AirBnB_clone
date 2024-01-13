#!/usr/bin/python3
"""The Console"""
import cmd
import re
from models.base_model import BaseModel
from models.user import User
from models import storage
from models.engine.file_storage import FileStorage

class HBNBCommand(cmd.Cmd):
    """creates a shell console for our models
    """
    prompt = "(hbnb) "
    __classes = ["Amenity", "BaseModel", "City", "Place", "Review", "State", "User"]
    __all_objs = storage.all()

    def emptyline(self) -> str:
        return ""

    def parse(self, line: str) -> list:
        # Both the regex below are almost same
        # matches = re.findall(r'("[^"]*"|[^\s"]*)', line) # adds '' (whitespace)
        lines = re.findall(r'("[^"]*"|\b[A-Za-z0-9_-]+\b)', line)
        return lines

    def do_all(self, line) -> None:
        """prints all string representation of all instances based or not
        on the class name
        """
        lines = self.parse(line)
        if (len(lines) == 0):
            objects = [k.__str__() for k in self.__all_objs.values()]
            print(objects)
        else:
            if (lines[0] in self.__classes):
                objects = [v.__str__() for k, v in self.__all_objs.items()
                           if k.split(".")[0] == lines[0]]
                print(objects)
            else:
                print("** class doesn't exist **")

    def do_create(self, line) -> None:
        """Creates a new instance of a given Class
        (saves it to the JSON file and prints the id)"""
        lines = self.parse(line)
        if (len(lines) == 0):
            print("** class name missing **")
        elif (lines[0] not in self.__classes):
            print("** class doesn't exist **")
        else:
            obj = eval(lines[0])()
            print(obj.id)
            obj.save()
            self.__all_objs = storage.all()

    def do_destroy(self, line) -> None:
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
                storage.save()

    def do_EOF(self, line) -> bool:
        """Quit command to exit the program"""
        return True

    def do_quit(self, line) -> bool:
        """Quit command to exit the program"""
        return True

    def do_show(self, line) -> None:
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

    def do_update(self, line) -> None:
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
                try:
                    setattr(obj, lines[2], eval(lines[3]))
                except NameError:
                    setattr(obj, lines[2], lines[3])
                eval(lines[0]).save(obj)
                # self.__all_objs = storage.all()


if __name__ == "__main__":
    HBNBCommand().cmdloop()
