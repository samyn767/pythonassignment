#! /usr/bin/python
from commands import commands

def main():
    print("CUSTOMER PORTAL TERMINAL")
    cmd = commands.Commands() 
    cmd.cmdloop()

if __name__ == "__main__":
    main()
