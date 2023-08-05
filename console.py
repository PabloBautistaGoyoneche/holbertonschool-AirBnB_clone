#!/usr/bin/python3
import cmd

class HBNBCommand(cmd.Cmd):
    prompt = '(hbnb)'
    completekey = None

    def _init_(self): 
        super()._init_()

    def emptyline(self):
        """ Test """
        pass

    def do_quit(self, line):
        print("Exit program")
        return True
    
    def do_create(self, line):
        if not line:
            print("** class name missing **")
            return
    
    def do_show(self, line):
        if not line:
            print("** class name missing **")
            return

    def do_destroy(self, line):
        if not line:
            print("** class name missing **")
            return

    def do_all(self, line):
        pass

    def do_update(self, line):
        pass
    
    def do_help(self, line):
        print("\n")
        print("Comandos documentados (escribe 'help <comando>'):")
        print("===============================================")
        print("EOF  help  quit  create  show  destroy  all  update")
        print("\n")

if __name__ == '__main__':
    HBNBCommand().cmdloop()
    
