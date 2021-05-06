#! /usr/bin/python
from commands import commands

def main():
    print("############################")
    print("# CUSTOMER PORTAL TERMINAL #")
    print("############################")
    cmd = commands.Commands() 
    cmd.cmdloop()

if __name__ == "__main__":
    main()
