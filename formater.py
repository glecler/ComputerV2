from __future__ import print_function
from sys import exec_prefix

class Formater :

    @staticmethod
    def format_expression(expression : str, functions : list) -> str :
        print("expression : ", expression)
        output = ''
        print_nb = 0
        print_alpha = 0
        print_neg_one = 0
        print_fun = 0
        buff = ''
        i = 0
        input = ''.join(expression.split())
        while i < len(input) :
            while i < len(input) and ((input[i] >= '0' and input[i] <= '9') or input[i] == ']'\
                or input[i] == '.' or input[i] == ' ' or input[i] == ':') :
                print_neg_one = 0
                if input[i] >= '0' and input[i] <= '9' and print_alpha == 1 :
                    output += ' * '
                    print_alpha = 0
                output += input[i]
                i += 1
                print_nb = 1
            while i < len(input) and input[i] >= 'a' and input[i] <= 'z' :
                buff += input[i]
                if print_neg_one == 1 and print_fun == 0 :
                    output += '1 * '
                if print_nb == 1 and print_fun == 0:
                    output += ' * '
                    print_nb = 0
                if print_nb == 1 and print_fun == 1:
                    output += '*'
                    print_nb = 0
                output += input[i]
                print_neg_one = 0
                print_alpha = 1
                i += 1
            if (True in [True if buff == j.name else False for j in functions]) :
                print_alpha = 0
                print_fun += 1
            buff = ''
            if i < len(input) :
                if (input[i] == '(' or input[i] == '[') and (print_nb == 1 or print_alpha == 1 or print_neg_one == 1) :
                    if print_neg_one == 1 :
                        output += '1'
                    output += ' * ' + input[i]
                    print_nb = 0
                    print_neg_one = 0
                    print_alpha = 0
                    i += 1
                elif (input[i] == ')') :
                    print_neg_one = 0
                    if print_fun > 0 :
                        output += '}'
                        print_fun -= 1
                    else :
                        output += input[i]
                    i += 1
                elif (input[i] == '(' or input[i] == '[') and (print_alpha == 0 and print_nb == 0 and print_neg_one == 0) :
                    char = '{' if print_fun > 0 and input[i] == '(' else input[i]
                    output += char
                    i += 1
                elif input[i] == '-' and  (print_nb == 1 or print_alpha == 1) :
                    output += ' - '
                    print_nb = 0
                    print_neg_one = 1
                    print_alpha = 0
                    i += 1
                elif input[i] == '-' and print_nb == 0 and print_alpha == 0 :
                    if print_neg_one == 1 :
                        output += '1 * '
                    print_neg_one = 1
                    output += '-'
                    i += 1
                elif input[i] == '^' :
                    print_nb = 0
                    print_alpha = 0
                    print_neg_one = 0
                    i += 1
                    output += '^'
                elif input[i] == '*' or input[i] == '/' or input[i] == '%' or input[i] == '+' :
                    if (i + 1 < len(input) and input[i + 1] == '*') :
                        output += '**'
                        i += 1
                    else :
                        output += ' ' + input[i] + ' '
                    print_nb = 0
                    print_alpha = 0
                    print_neg_one = 0
                    i += 1
                elif input[i] == ',' or input[i] == ';' :
                    output += input[i]
                    print_nb = 0
                    print_alpha = 0
                    print_neg_one = 0
                    i += 1
                elif input[i] == '{' or input[i] == '}' :
                    output += input[i]
                    i += 1
        return output


        #   def format_expression(expression : str, functions : list) -> str :
        #output = ''
        #print_nb = 0
        #print_alpha = 0
        #buff = ''
        #i = 0
        #input = ''.join(expression.split())
        #while i < len(input) :
        #   while i < len(input) and ((input[i] >= '0' and input[i] <= '9') or input[i] == ')' or input[i] == ']'\
        #       or input[i] == '.') :
        #       output += input[i]
        #       i += 1
        #       print_nb = 1
        #   while i < len(input) and input[i] >= 'a' and input[i] <= 'z' :
        #       buff += input[i]
        #       if print_nb == 1 :
        #           output += ' * '
        #           print_nb = 0
        #       output += input[i]
        #       print_alpha = 1
        #       i += 1
        #   if (True in [True if buff == j.name else False for j in functions]) :
        #       print_alpha = 0
        #   buff = ''
        #   if i < len(input) :
        #       if (input[i] == '(' or input[i] == '[') and (print_nb == 1 or print_alpha == 1) :
        #           output += ' * '+ input[i]
        #           print_nb = 0
        #           print_alpha = 0
        #           i += 1
        #       elif (input[i] == '(' or input[i] == '[') and (print_alpha == 0 and print_nb == 0) :
        #           output += input[i]
        #           i += 1
        #       elif input[i] == '-' and  (print_nb == 1 or print_alpha == 1) :
        #           output += ' - '
        #           print_nb = 0
        #           print_alpha = 0
        #           i += 1
        #       elif input[i] == '-' and print_nb == 0 and print_alpha == 0 :
        #           output += '-'
        #           i += 1
        #       elif input[i] == '^' :
        #           print_nb = 0
        #           print_alpha = 0
        #           i += 1
        #           output += '^'
        #       elif input[i] == '*' or input[i] == '/' or input[i] == '%' or input[i] == '+' :
        #           output += ' ' + input[i] + ' '
        #           print_nb = 0
        #           print_alpha = 0
        #           i += 1
        #       elif input[i] == ',' or input[i] == ';' :
        #           output += input[i]
        #           print_nb = 0
        #           print_alpha = 0
        #           i += 1
        #return output
