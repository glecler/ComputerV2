#!/usr/bin/python3

class Function():

    def __init__(self, name, input, arglist):
        self.name = name.split('(', 1)[0]
        self.arg = name.split('(')[1].split(')')[0]
        self.expression = input
        self.arglist = arglist
        print(f"{self.name}({self.arg}) = {self.expression}")
        
    def image(self, x: str) -> str:
        y = self.expression.replace('x', str(x))
        # reduce (-- => +)
        return(y)
