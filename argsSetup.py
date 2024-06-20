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
    
    '''
    Flag: -m
    Def: Number of characters in each input file is written to the standard output
    '''
    parser.add_argument('-m',
                        nargs='?',
                        type=argparse.FileType("r"),
                        const=sys.stdin,
                        help="Number of characters in each input file is written to the standard output"
                        )
    '''
    Flag: -l
    Def: Number of lines in each input file is written to the standard output
    '''
    parser.add_argument('-l',
                        nargs='?',
                        type=argparse.FileType("r"),
                        const=sys.stdin,
                        help="Number of lines in each input file is written to the standard output"
                        )
    '''
    Flag: -w
    Def: Number of words in each input file is written to the standard output
    '''
    parser.add_argument('-w',
                        nargs='?',
                        type=argparse.FileType("r"),
                        const=sys.stdin,
                        help="Number of words in each input file is written to the standard output")
    
    '''
    Positional, default argument if no -flag
    Def: Displays Number of Lines, Words, Bytes, in that order
    '''
    parser.add_argument('input_file',
                        nargs='?',
                        help="Displays Number of Lines, Words, Bytes, in that order")
    
    args = parser.parse_args()
    return args