# ########################################################################## #
#                                                                            #
#                                                        :::      ::::::::   #
#   solver.py                                          :+:      :+:    :+:   #
#                                                    +:+ +:+         +:+     #
#   By: glecler <glecler@student.42.fr>            +#+  +:+       +#+        #
#                                                +#+#+#+#+#+   +#+           #
#   Created: 2021/11/10 by glecler                    #+#    #+#             #
#   Updated: 2021/11/10 by glecler                   ###   ########.fr       #
#                                                                            #
# ########################################################################## #

class Member:
    def __init__(self, factors, powers):
        self.factors = factors
        self.powers = powers

class Solver:
    def __init__(self, left: Member, right: Member) -> None:
        self.reduced_form = self.reduce_form(left, right)
        self.degree = self.get_degree()
    
    def fill_form(self, right, left) :

        right_buff = Member(['0', '0', '0'], ['0', '1', '2'])
        left_buff = Member(['0', '0', '0'], ['0', '1', '2'])
        for i in range(len(right.powers)) :
            right_buff.factors[int(right.powers[i])] = right.factors[i]
        for i in range(len(left.powers)) :
            left_buff.factors[int(left.powers[i])] = left.factors[i]
        print("tests : ", right_buff, left_buff)
        return right_buff, left_buff
        

    def reduce_form(self, left: Member, right: Member) -> Member:
        print("before", left.factors, left.powers,right.factors, right.powers)
        (right, left) = self.fill_form(right, left)
        (left, right) = self.equalize_degree(left, right)
        
        print("after", left.factors, left.powers,right.factors, right.powers)
        reduced_form_factors = Member([], [])
        ## this is assuming factors and powers are set to 0
        for i in range(len(right.powers)) :
            reduced_form_factors.factors.append(str(float(left.factors[i]) - float(right.factors[i])))
            reduced_form_factors.powers.append(left.powers[i])
        print("reduced : ", reduced_form_factors.factors, reduced_form_factors.powers)
        return(reduced_form_factors)

    def equalize_degree(self, left: Member, right: Member):
        length = max(int(max(left.powers)), int(max(right.powers)))
        print("length : ", length)
        if int(max(left.powers)) < int(max(right.powers)):
            swap = right
            right = left
            left = swap
        for i in range(int(max(right.powers)) + 1, length):
            right.powers.append(str(i))
            right.factors.append('0')
        return left, right

    def get_degree(self) -> int:
        degree = -1

        for i in range(len(self.reduced_form.powers)):
            if float(self.reduced_form.factors[i]) != 0:
                degree = int(self.reduced_form.powers[i])
        return degree

    def print_reduced_form_degree(self) -> None:
        sign = ''
        print("Reduced form : ", end='')
        next_sign = True
        if self.degree >= 0:
            for i in range(self.degree):
                if abs(float(self.reduced_form.factors[i])) == 0:
                    next_sign = False
                    continue
                if float(self.reduced_form.factors[i]) < 0 and i > 0 and next_sign:
                    sign = " - "
                elif float(self.reduced_form.factors[i]) < 0 and i == 0 and next_sign:
                    sign = "-"
                elif float(self.reduced_form.factors[i]) >= 0 and i > 0 and next_sign:
                    sign = " + "
                print(sign + str(abs(float(self.reduced_form.factors[i]))) + " * X^" + self.reduced_form.powers[i], end='')
                next_sign = True
        else :
            print("0", end='')
            self.degree = 0
        print(" = 0")
        print("Polynomial degree :", self.degree)

    def solve_degree_two(self) -> None:
        delta = (float(self.reduced_form.factors[1]) * float(self.reduced_form.factors[1])) \
                - 4 * float(self.reduced_form.factors[2]) * float(self.reduced_form.factors[0])
        match delta:
            case delta if delta > 0:
                print('Discriminant is stricly positive, the two solutions are:\n', \
                        (-1 * float(self.reduced_form.factors[1]) - self.sqrt(delta)) / \
                        (2 * float(self.reduced_form.factors[2])), '\nand :\n', (-1 * float(self.reduced_form.factors[1]) \
                        + self.sqrt(delta)) / (2 * float(self.reduced_form.factors[2])))
            case 0:
                print('Discriminant is zero, the unique solution is:\n', \
                        (-1 * float(self.reduced_form.factors[1])) / (2 * float(self.reduced_form.factors[2])))
            case delta if delta < 0:
                print('Discriminant is stricly negative, the two solutions are:\n', \
                        (-1 * float(self.reduced_form.factors[1])) / (2 * float(self.reduced_form.factors[2])), \
                        ' + i * ' , self.sqrt(abs(delta)) / (2 * float(self.reduced_form.factors[2])), \
                        '\nand :\n', (-1 * float(self.reduced_form.factors[1])) / (2 * float(self.reduced_form.factors[2])), \
                        ' - i * ' , self.sqrt(abs(delta)) / (2 * float(self.reduced_form.factors[2])))

    def solve(self) -> None:
        if self.degree == 2:
            self.solve_degree_two()
        elif self.degree >= 3:
            print('The polynomial degree is stricly greater than 2, I can\'t solve')
        elif self.degree == 0 and float(self.reduced_form.factors[0]) != 0:
            print('No solution.')
        elif self.degree == 0 and float(self.reduced_form.factors[0]) == 0:
            print('The solution is : x E |R.')
        elif self.degree == 1 and float(self.reduced_form.factors[1]) != 0:
            print('The solution is : \nx = ', float(self.reduced_form.factors[0])/\
                    float((-1 * float(self.reduced_form.factors[1]))))
        else:
            print('Could not divide by 0')

    @staticmethod
    def sqrt(f):
        tmp = 0
        f2 = f / 2

        while(f2 != tmp):
            tmp = f2
            f2 = (f / tmp + tmp) / 2
        return f2
