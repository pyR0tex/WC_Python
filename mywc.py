# mywc.py
'''
Python clone of the UNIX program: * wc *

Author: Rohit Cheruku
'''

# Imports
from argsSetup import argsSetup

def main(args):
    """ Python clone of the UNIX program: * wc * """
    print(" Python clone of the UNIX program: * wc * ")
    if args.echo:
        print("hello")
    pass

if __name__ == '__main__':
    args = argsSetup()

    main(args)