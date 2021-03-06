#!/usr/bin/python3

# Variables
# Matrices structure
# Functions

# Console
# Parser
# Calculator

from interpreter import *

def prompt() :
    cmd = input('> ')
    return cmd

def main() :
    cmd = 0
    interpreter = Interpreter()

    while cmd != 'quit' :
        cmd = prompt()
        print(interpreter.parse(cmd))

if __name__ == '__main__' :
    main()