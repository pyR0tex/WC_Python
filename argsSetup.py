# argsSetup.py

'''
- Helper script for mywc
- Sets up the arguments this app will take to be used by mywc
'''

import argparse
import sys

def argsSetup():
    
    parser = argparse.ArgumentParser(
        description="Python clone of the UNIX program: * wc *"
    )
    parser.add_argument('echo', type=str, nargs='*', help='echoing')
    args = parser.parse_args()
    return args