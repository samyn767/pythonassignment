from cmd import Cmd
import sys
import shlex

from . import dls, dset
from repositories.helpers import bcolors

class Commands(Cmd):
    prompt = bcolors.HEADER + 'Customer Portal Terminal# ' + bcolors.ENDC
    intro = bcolors.HEADER + 'Welcome To Dhiraagu Customer Portal Terminal.\n---------------------------------------------' + bcolors.ENDC

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
