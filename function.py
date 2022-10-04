#!/usr/bin/python3
import math as mt

class Function :

    def __init__(self, name, input) :
        self.name = name.split('(', 1)[0]
        self.arg = name.split('(')[1].split(')')[0]
        self.expression = input # here should 
    
    def image(self, x : str) -> str :
        buff = ''
        i = 0
        exp_buff = self.expression
        while i < len(exp_buff) :
            if exp_buff[i] == self.arg :
                if buff == '' or buff == ' ' or buff == '{' or buff == '(':
                    if (i + 1 < len(exp_buff) and (exp_buff[i + 1] == ' ' or \
                        exp_buff[i + 1] == '}' or exp_buff[i + 1] == ')' or exp_buff[i + 1] == '^')) or i + 1 >= len(exp_buff[i]) :
                        exp_buff = exp_buff[:i] + '(' + str(x) + ')' + exp_buff[i + 1:]
            buff = exp_buff[i]
            i += 1
        return exp_buff
        
    def __str__(self) :
        # maybe simplify expressions here
        return f'{self.expression}'

class Cosinus(Function) :
    def image(self, x: str) -> str:
        if type(x) != str :
            return
        return str(mt.cos(float(x)))

class Sinus(Function) :
    def image(self, x: str) -> str:
        return str(mt.sin(float(x)))

class Exp(Function) :
    def image(self, x : str) :
        return str(mt.exp(float(x)))

class Sqrt(Function) :
    def image(self, x : str) :
        return str(mt.sqrt(float(x)))
