#!/usr/bin/python3

# Variables
# Matrices structure
# Functions

# Console
# Parser
# Calculator

from interpreter import Interpreter

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OK = OKGREEN + '[OK]' + ENDC
    KO = FAIL + '[KO]' + ENDC


def prompt() :
    cmd = input('> ')
    return cmd

def main() :
    cmd = 0
    interpreter = Interpreter()
    colors = Colors

    while cmd != 'quit' :
        cmd = prompt()
        buff = interpreter.parse(cmd)
        comment = colors.OKCYAN + interpreter.status + colors.ENDC + '\n'
        print(comment + buff)

if __name__ == '__main__' :
    main()
