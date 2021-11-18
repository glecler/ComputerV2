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
		self.print_reduced_form_degree()

	def reduce_form(self, left: Member, right: Member) -> Member:
		(left, right) = self.equalize_degree(left, right)
		reduced_form_factors = left
		for i in range(len(right.factors)):
				reduced_form_factors.factors[i] = str(float(left.factors[i]) - float(right.factors[i]))
		return(reduced_form_factors)

	def equalize_degree(self, left: Member, right: Member):
		length = max(int(max(left.powers)), int(max(right.powers)))
		if int(max(left.powers)) < int(max(right.powers)):
			swap = right
			right = left
			left = swap
		for i in range(int(max(right.powers)) + 1, length + 1):
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
			for i in range(self.degree + 1):
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