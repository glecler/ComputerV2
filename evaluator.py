#!/usr/bin/python3

from types import FrameType
from variables import *
from formater import Formater
from error import Error, SilentError

class Evaluator:

	def __init__(self, arglist : list, functions : list) :
		self.arglist = arglist
		self.functions = functions
		self.formater = Formater()
	
	# find, evaluates then replace function image in expression
	def ft_eval_functions(self, exp : str) -> str :
		sp = exp.split()
		i = -1
		while i < len(sp) - 1:
			i += 1
			if '(' in sp[i] and ')' in sp[i] : # 'f(x)'
				func_name, func_arg = self.ft_trim_function(sp[i])
				is_name = False
				print('name : ', func_name)
				for k in self.functions :
					if func_name == k.name :
						is_name = True
						if func_arg == k.arg :
							print(k.expression)
							return 0 # g(x) = 3 * x
						if func_name == 'cos' or func_name == 'sin' :
							print('yuk')
							func_arg = self.ft_eval(func_arg)
						print('ok : ', k.image(func_arg))
						if type(eval_func := self.ft_eval(k.image(func_arg))) == Error :
							return eval_func
						sp[i] = sp[i].replace(func_name + '(' + func_arg + ')', str(eval_func))
						i = 0
				if is_name is False and func_name != '' :
					return Error(7)
		return self.formater.format_expression(''.join(sp), self.functions)
	
	# find variable in the split on ^ for eval_powers
	def ft_get_argument(self, exp : str) -> str :
		x = 0
		brack = 0
		buff = ''
		if exp[x] == '(' :
			brack = brack + 1
			x = x + 1
			while brack != 0 :
				if exp[x] == '(' :
					brack = brack + 1
				if exp[x] == ')' :
					brack = brack - 1
				x = x + 1
			buff = exp[:x + 1]
		elif exp[x] == ')' :
			brack = brack + 1
			x = x + 1
			while brack != 0 :
				if exp[x] == ')' :
					brack = brack + 1
				if exp[x] == '(' :
					brack = brack - 1
				x = x + 1
			while x < len(exp) and exp[x] >= 'a' and exp[x] <= 'z' :
				x += 1
			buff = exp[:x + 1].strip('*')
			print(buff)
		else :
			while x < len(exp) and ((exp[x] >= 'a' and exp[x] <= 'z') \
				or (exp[x] >= '0' and exp[x] <= '9') \
					or (exp[x] =='(' or exp[x] == ')') or exp[x] == '.') :
				buff = buff + exp[x]
				x = x + 1
		return buff

	# adds brackets where needed
	def ft_even_bracket(self, exp : str) :
		brack = 0
		buff = exp.strip()
		for i in buff :
			if i == '(' : 
				brack += 1
			if i == ')' :
				brack -= 1
		while brack != 0 :
			if brack > 0 :
				buff += ')'
				brack -= 1
			if brack < 0 :
				buff = '(' + buff
				brack += 1
		return buff

	# cuts exp on ^ and evals left and right arguments, then replace into expression
	def ft_eval_powers(self, exp : str) :
		print(exp)
		left = self.ft_get_argument(exp.rsplit('^', 1)[0][::-1])[::-1] # rev rev
		right = self.ft_get_argument(exp.rsplit('^', 1)[1])
		buff_left = self.ft_even_bracket(left)
		buff_right = self.ft_even_bracket(right)
		print(buff_right, buff_left)
		buff = str(self.ft_eval(buff_left)**self.ft_eval(buff_right))
		print(buff)
		return exp.replace(left + '^' + right, buff)

	# evaluates any expression and returns a variable
	def ft_eval(self, exp : str) :
		while '^' in exp :														
			exp = self.ft_eval_powers(exp)
		print('a', exp)
		if (exp := self.ft_eval_functions(exp)) != 0 :
			if type(exp) is Error :
				return exp
		else :
			return SilentError(0)
		if '(' not in exp :
			return self.ft_eval_exp(exp)														
		i = 0
		while '(' in exp[i:] :
			i += 1
		j = i
		while j < len(exp) and exp[j] != ')' :
			j += 1
		exp = exp.replace(exp[i - 1:j + 1], repr(self.ft_eval_exp(exp[i:j])))
		if '(' not in exp :
			return self.ft_eval_exp(exp)
		return self.ft_eval(exp)
	
	# recursive parser, works on expression without brackets
	# splits the expression until only variables remain then return the variable, performing the calculation recursively
	def ft_eval_exp(self, exp : str) :
		if '+' in exp :
			return self.ft_eval_exp(exp.split('+', 1)[1]) + \
				self.ft_eval_exp(exp.split('+', 1)[0])
		if self.split_on_last_sub(exp) :
			return self.ft_eval_exp(self.split_on_last_sub(exp)[0]) - \
				self.ft_eval_exp(self.split_on_last_sub(exp)[1])
		if '*' in exp or '/' in exp or '%' in exp :
			for i in exp :
				if '/' == i :
					return self.ft_eval_exp(exp.rsplit('/', 1)[0]) / \
						self.ft_eval_exp(exp.rsplit('/', 1)[1])
				if '%' == i :
					return self.ft_eval_exp(exp.rsplit('%', 1)[0]) % \
						self.ft_eval_exp(exp.rsplit('%', 1)[1])
				if '*' == i :
					return self.ft_eval_exp(exp.rsplit('*', 1)[0]) * \
						self.ft_eval_exp(exp.rsplit('*', 1)[1])
		for i in range(len(self.arglist)) :
			if self.arglist[i].name in exp :
				return self.arglist[i].copy()
		if '{' in exp :
			return self.ft_eval_functions(exp)
		if '[' in exp :
			if '[[' in exp :
				return Matrix('', exp)
			else :
				return Imaginaries('', float(exp.split(',')[0].strip().strip('[')), \
					float(exp.split(',')[1].strip().strip(']')))
		if True in [True for i in exp.strip() if 'z' >= i >= 'a'] :
			return Error(9)
		if exp == '' :
			return Rationnals('', 0)
		if self.isfloat(''.join(exp.split())) == False :
			return Rationnals('', 0) #Error(16)
		return Rationnals('', float(''.join(exp.split())))
	
	@staticmethod
	def ft_trim_function(exp : str) :
		i = 0
		while exp[i] == '(':
			i += 1
		if '(' in exp[i:] :
			func_name = exp[i:].split('(', 1)[0]
			j = 0
			#print(func_name)
			while func_name[j] <= 'a' or func_name[j] >= 'z' or func_name[j] == 'i' :
				j += 1
			#print('aaaa', func_name, func_name[:j])
			func_name = func_name[j:]
			func_arg = exp[i:].split('(', 1)[1].split(')', 1)[0] # TODO find matching brackets
			return func_name, func_arg
		return '', ''

	@staticmethod
	def split_on_last_sub(exp : str) -> tuple :
		last_char = 'start'
		split_index = 0
		for i in range(len(exp)) :
			if exp[i] == '-' and last_char == 'numeric' :
				split_index = i
				last_char = '-'
			if exp[i] == '*' or exp[i] == '/' or exp[i] == '%' \
				or exp[i] == ',' or exp[i] == ';' or exp[i] == ']' or exp[i] == '[' :
				last_char = '*/%'
			if '9' >= exp[i] >= '0' or 'z' >= exp[i] >= 'a' : #check arguments
				last_char = 'numeric'
		if split_index == 0 :
			return 0
		return exp[:split_index - 1], exp[split_index + 1:]


	@staticmethod
	def isfloat(value : str) -> bool :
		try :
			float(value)
			return True
		except ValueError :
			return False