# mywc.py
''' 
Python clone of the UNIX program: * wc *

Author: Rohit Cheruku
'''

# Imports
from argsSetup import argsSetup
from os import path, remove
import sys

def main(args):
    """ Python clone of the UNIX program: * wc * """
    #print(" Python clone of the UNIX program: * wc * ")
    
    # Start of if cases for input file / flags
    # if -c flag
    if args.c:
        if args.c.name != "<stdin>":
            print(f"      {Byte_Count(args.c.name)} {path.basename(args.c.name)}")
        else:
            print(f"      {Byte_Count(args.c.name)}")
    elif args.m:
        if args.m.name != "<stdin>":
            print(f"      {Char_Count(args.m.name)} {path.basename(args.m.name)}")
        else:
            print(f"      {Char_Count(args.m.name)}")
    else:
        if args.input_file:
            print(f"{args.input_file}")
        else:
            print(f"        input -> stdin: feature = work in progress")

def Byte_Count(fileName):
    ''' Returns the number of bytes in each Input File

    Parameters:
        fileName (str): standard input (stdin) or Path to a file

    Return:
        str: number of bytes in file
    
    Exceptions:
        FileNotFoundError: If file not found or name is invalie
        OSError: If any other exception occurs
    '''
    try:
        if fileName == "<stdin>":
            stdinContent = sys.stdin.read()

            numBytes = len(bytes(stdinContent, "utf-8"))

            return str(numBytes)
        
        else:
            try:
                numBytes = path.getsize(fileName)

                return numBytes
            
            except FileNotFoundError:
                return f"File: {path.basename(fileName)} not found"
            
    except OSError:
        return "OS Error occurred"

def Char_Count(fileName):
    ''' Returns the number of characters in each Input File

    Parameters:
        fileName (str): standard input (stdin) or Path to a file

    Return:
        str: number of characters in file
    
    Exceptions:
        FileNotFoundError: If file not found or name is invalie
        OSError: If any other exception occurs
    '''
    countChars = 0
    try:
        if fileName == "<stdin>":
            stdinContent = sys.stdin.read().encode("utf-8")

            for char in stdinContent:
                countChars += 1

            return countChars
        
        else:
            try:
                with open(fileName, "r") as File:
                    for line in File:
                        countChars += len(line.encode("utf-8"))

                    return countChars
                
            except FileNotFoundError:
                return(f"File: {path.basename(fileName)} not found")
    except OSError:
        return "OS Error occurred"

if __name__ == '__main__':
    # Get list of arguments for argparse
    args = argsSetup()
    main(args)