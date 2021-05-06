from cmd import Cmd
from . import dls, dset

class Commands(Cmd):
    prompt = 'Customer Portal Terminal# '
    intro = 'Welcome To Dhiraagu Customer Portal Terminal.'

    def do_exit(self, inp):
        '''Exit The Customer Portal Terminal.'''
        print("GOODBYE!!")
        return True

    def help_exit(self):
        print('Exit the application. Ctrl-D.')

    def do_dls(self, inp):
        '''List And Search Customers.'''
        dls.execute()

    def do_dset(self, inp):
        '''Update Customer Details.'''
        dset.execute()

    do_EOF = do_exit
    help_EOF = help_exit
