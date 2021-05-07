#! /usr/bin/python
from commands import commands
from repositories.helpers import bcolors

def main():
    print(f"{bcolors.HEADER}----------------------------\n| CUSTOMER PORTAL TERMINAL |\n----------------------------{bcolors.ENDC}")
    cmd = commands.Commands() 
    cmd.cmdloop()

if __name__ == "__main__":
    main()
