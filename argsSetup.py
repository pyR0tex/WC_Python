# argsSetup.py

'''
- Helper script for mywc
- Sets up the arguments this app will take to be used by mywc
'''

import argparse
import sys

def argsSetup():
    '''
    Initialize an instance of argparse
    parser: container for argument specification and has 
            options that apply to parser as a whole
    '''
    parser = argparse.ArgumentParser(
        prog="mywc",
        description="Python clone of the UNIX program: * wc *"
    )
   
    '''
    Flag: -c
    Def: Number of bytes in each input file is written to the standard output
    '''
    parser.add_argument('-c',
                        nargs='?',
                        type=argparse.FileType("r"),
                        const=sys.stdin,
                        help="The number of bytes in each input file is written to standard output"
                        )
    
<<<<<<< HEAD
=======
    '''
    Flag: -m
    Def: Number of characters in each input file is written to the standard output
    '''
    
    '''
    Flag: -l
    Def: Number of lines in each input file is written to the standard output
    '''

    '''
    Flag: -w
    Def: Number of words in each input file is written to the standard output
    '''

>>>>>>> 9f3ec6850628a957a76118dd5f634cc8831d244e
    args = parser.parse_args()
    return args