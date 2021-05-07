from cmd import Cmd
import sys
from . import dls, dset
import shlex

class Commands(Cmd):
    prompt = 'Customer Portal Terminal# '
    intro = 'Welcome To Dhiraagu Customer Portal Terminal.\n---------------------------------------------'

    def do_exit(self, inp):
        '''Exit The Customer Portal Terminal.'''
        print("GOODBYE!!")
        return True

    def emptyline(self):
         pass

    def help_exit(self):
        print('Exit the application. Ctrl-D.')

    def do_dls(self, inp):
        dls.execute(shlex.split(inp))

    def help_dls(self):
        dls.parser.print_help()

    def do_dset(self, inp):
        dset.execute(shlex.split(inp))

    def help_dset(self):
        dset.parser.print_help()

    do_EOF = do_exit
    help_EOF = help_exit
