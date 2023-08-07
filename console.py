#!/usr/bin/python3

""" This is the command interpreter """

import cmd
from models.base_model import BaseModel
from models.engine.file_storage import FileStorage
from models.user import User
from models.state import State
from models.review import Review
from models.place import Place
from models.city import City
from models.amenity import Amenity


class HBNBCommand(cmd.Cmd):

    """Interpreter class from cmd"""

    def emptyline(self):
        """Overrides parent empty line method"""
        pass

    prompt = '(hbnb)'

    classes_list = ["BaseModel", "User", "State", "City",
                    "Amenity", "Place", "Review"]

    int_attrs = ["attribute1", "attribute2"]
    float_attrs = ["attribute3", "attribute4"]

    prompt = '(hbnb) '
    completekey = None

    def _init_(self):
        super()._init_()

    def emptyline(self):
        """Overrides parent empty line method"""
        pass

    def do_EOF(self, line):
        """Quits the console when Ctrl D entered"""
        print()
        return True

    def do_quit(self, line):
        """Quit command to exit the program"""
        return True

    def do_create(self, line):
        """Creates a new instance of a specified class and prints
        nstance's unique id"""
        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return

        new_obj = globals()[args[0]]()
        new_obj.save()
        print(new_obj.id)

    def do_show(self, line):
        """Prints the string repr of an instance based
        on class name and id"""
        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_key = args[0] + "." + args[1]
        storage = FileStorage()
        all_objs = storage.all()

        for key, value in all_objs.items():
            if key == obj_key:
                print(value)
                return
        print("** no instance found **")

    def do_destroy(self, line):
        """Deletes an instance of a class based on class name and id"""
        if not line:
            print("** class name missing **")
            return
        args = line.split()
        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_key = args[0] + "." + args[1]
        storage = FileStorage()
        all_objs = storage.all()
        for key, value in all_objs.items():
            if key == obj_key:
                del all_objs[key]
                storage.__objects = all_objs
                storage.save()
                return
        print("** no instance found **")

    def do_all(self, line):
        """Prints, as a list of strings, or all instances of a certain
        class, if provided"""
        objs_list = []
        storage = FileStorage()
        all_objs = storage.all()
        check = False

        if not line:
            for key, value in all_objs.items():
                objs_list.append(str(value))

            print(objs_list)
            return
        else:
            args = line.split()

            for key, value in all_objs.items():
                test_obj_type = key.split(".")
                if test_obj_type[0] == args[0]:
                    objs_list.append(str(value))
                    check = True
                if check:
                    print(objs_list)
                else:
                    print("** class doesn't exist **")

    def do_update(self, line):

        """ Updates or adds an attribute to an instance of a class.
        The instance is identified by the class name and the id.
        You can only update one attribute and one value per call """

        if not line:
            print("** class name missing **")
            return

        args = line.split()

        if args[0] not in HBNBCommand.classes_list:
            print("** class doesn't exist **")
            return

        if len(args) < 2:
            print("** instance id missing **")
            return

        obj_key = args[0] + "." + args[1]
        storage = FileStorage()
        all_objs = storage.all()
        instance_found = False

        for key, value in all_objs.items():
            if key == obj_key:
                instance_found = value

        if not instance_found:
            print("** no instance found **")
            return

        if len(args) < 3:
            print("** attribute name missing **")
            return

        if len(args) < 4:
            print("** value missing **")
            return

        if args[2] in HBNBCommand.int_attrs:
            setattr(instance_found, args[2], int(args[3]))
        elif args[2] in HBNBCommand.float_attrs:
            setattr(instance_found, args[2], float(args[3]))
        else:
            setattr(instance_found, args[2], args[3])

        instance_found.save()

    def do_help(self, line):
        print("\n")
        print("Comandos documentados (escribe 'help <comando>'):")
        print("===================================================")
        print("EOF  help  quit  create  show  destroy  all  update")
        print("\n")


if __name__ == '__main__':
    HBNBCommand().cmdloop()
