#!/usr/bin/python3
import math as mt

class Function :

    def __init__(self, name, input) :
        self.name = name.split('(', 1)[0]
        self.arg = name.split('(')[1].split(')')[0]
        self.expression = input
        
    def image(self, x : str) -> str :
        return self.expression.replace(self.arg, str(x))
        
    def __str__(self) :
        return f'{self.expression}'

class Cosinus(Function) :
    def image(self, x: str) -> str:
        return str(mt.cos(float(x)))

class Sinus(Function) :
    def image(self, x: str) -> str:
        return str(mt.sin(float(x)))