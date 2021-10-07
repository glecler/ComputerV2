#!/usr/bin/python3

from variables import *
from formater import Formater
from error import Error

class Evaluator():

	def __init__(self, arglist, functions):
		self.arglist = arglist
		self.functions = functions
		self.formater = Formater()

	def ft_eval_brackets(self, exp) -> float:
		if '(' not in exp and ')' not in exp:
			return(self.ft_eval(exp))



		right_bracket = [True for l in exp if l == '(']
		left_bracket = [True for l in exp if l == ')']
		if len(right_bracket) != len(left_bracket):
			return(Error(8))
		


		sp = exp.split()
		#print(sp)
		for i in range(len(sp)):
			if '(' in sp[i] and ')' in sp[i]:
				j = 0
				while sp[i][j] == '(':
					j += 1
				if '(' not in sp[i][j:]:
					pass
				else:
					func_name = sp[i][j:].split('(', 1)[0]
					is_name = False
					for k in self.functions:
						if func_name == k.name:
					#print(f'{func_name = }')
							is_name = True
							func_arg = sp[i][j:].split('(', 1)[1].split(')', 1)[0]
							sp[i] = self.formater.format_expression(sp[i][:j] + str(self.ft_eval_brackets(k.image(func_arg))) + sp[i][j:].split('(', 1)[1].split(')', 1)[1])
					if is_name is False and func_name != '':
						return Error(7)

		exp = self.formater.format_expression("".join(sp))

		#print(exp)
		if '(' not in exp:
			return(self.ft_eval(exp))
		for i in range(len(exp)):
			while '(' in exp[i:]:
				i += 1
			j = i
			while exp[j] != ')':
				j += 1
			exp = exp.replace(exp[i - 1:j + 1], repr(self.ft_eval(exp[i:j])))
			#print(exp)
			i = 0
			if '(' not in exp:
				return(self.ft_eval(exp))
			else:
				return(self.ft_eval_brackets(exp))

	def isfloat(self, value):
		try:
			float(value)
			return True
		except ValueError:
			return False
	
	def ft_eval(self, exp) -> Variable: # complex? create class for variable
		#print(exp)
		if '+' in exp:
			return(self.ft_eval(exp.split('+', 1)[1]) + self.ft_eval(exp.split('+', 1)[0]))
		if self.split_on_last_sub(exp):
			return(self.ft_eval(self.split_on_last_sub(exp)[0]) - self.ft_eval(self.split_on_last_sub(exp)[1]))
		if '*' in exp or '/' in exp or '%' in exp :
			for i in exp:
				if '/' == i:
					return(self.ft_eval(exp.rsplit('/', 1)[0]) / self.ft_eval(exp.rsplit('/', 1)[1]))
				if '%' == i:
					return(self.ft_eval(exp.rsplit('%', 1)[0]) % self.ft_eval(exp.rsplit('%', 1)[1])) # create methods for that
				if '*' == i:
					return(self.ft_eval(exp.rsplit('*', 1)[0]) * self.ft_eval(exp.rsplit('*', 1)[1]))
		for i in range(len(self.arglist)):
			if self.arglist[i].name in exp:
				#print(self.arglist[i])
				return(self.arglist[i]) # return class
		if "[" in exp:
			# put matrices here as well
			# parse for difference
			#print(float(exp.split(',')[1].strip().strip(']')))
			return(Imaginaries("", float(exp.split(',')[0].strip().strip('[')), float(exp.split(',')[1].strip().strip(']'))))
		#print("".join(exp.split()))
		#if 'x' in exp:
		#	return(Unknown(exp))
		g = [True for i in exp if 'z' > i > 'a']
		if True in g:
			return Error(9)
		else:
			return (Rationnals("", float("".join(exp.split()))))
		
	@staticmethod
	def split_on_last_sub(exp: str) -> tuple:
		last_char = 'start'
		split_index = 0
		for i in range(len(exp)):
			if exp[i] == '-' and last_char == 'numeric':
				split_index = i
				last_char = '-'
			if exp[i] == '*' or exp[i] == '/' or exp[i] == '%' or exp[i] == ',':
				last_char = '*/%'
			if '9' > exp[i] > '0' or exp[i] == 'i':
				last_char = 'numeric'
			i += 1
		if split_index == 0:
			return 0
		return (exp[:split_index - 1], exp[split_index + 1:])

