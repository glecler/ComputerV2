#!/usr/bin/python3
from typing import Optional
from function import *
from variables import *
from evaluator import *
from formater import Formater
from error import Error

class Interpreter:
	
	def __init__(self, input):
		self.functions = []
		self.arglist = []
		self.arglist.append(Imaginaries("i", 0, 1))
		self.evaluator = Evaluator(self.arglist, self.functions)
		self.formater = Formater()
		
	def check_function_format(self, function: str, expression: str) -> bool:
		var = ''
		if ' ' in function:
			return False
		i = 0
		while function[i] >= 'a' and function[i] <= 'z':
			var += function[i]
			i += 1
		if function[i] == '(':
			i += 1
			while function[i] >= 'a'and function[i] <= 'z':
				i += 1
		if function[i] == ')':
			return True
		return False

	def parse_function(self, left_cmd: str, right_cmd: str) -> int:
		# check function format f(x) = something
		# assign formated (evaled as much as possible)
		# check right member validity = only numerical + matrix + functions + arg of function
		if self.check_function_format(left_cmd, right_cmd):
			exp = self.formater.format_expression(right_cmd).split()
			for i in range(len(exp)):
				for arg in self.arglist:
					if exp[i] == arg.name:
						exp[i] = str(arg)
			input = self.formater.format_expression("".join(exp))
			for i in range(len(self.functions)):
				if self.functions[i].name == left_cmd:
					self.functions[i] = Function(left_cmd, input, self.arglist)
					return 0
			self.functions.append(Function(left_cmd, input, self.arglist))

		else:
			return Error(2)
		return 0


#Imaginaries(left_cmd, float(right_cmd.split('i')[0].strip().strip('+').strip('-').strip()), float(right_cmd.split('i')[1].strip('*').strip()))
	def parse_variable(self, left_cmd: str, right_cmd: str) -> int:
		# variables here : R, C, matrix
		# check left member only alpha and not i
		# eval right member and assign to left member
		# if left member not already a variable, append, else reassign
		for i in range(len(self.arglist)):
			if self.arglist[i].name == left_cmd:
				self.arglist[i] = self.evaluator.ft_eval_brackets(right_cmd)
				self.arglist[i].name = left_cmd
				#print(i)
				return 0
		if 'i' in right_cmd:
			arg = self.evaluator.ft_eval_brackets(right_cmd)
			arg.name = left_cmd
			self.arglist.append(arg)
			print(self.arglist)
			return 0
			# find r and i parts
			# self.arglist.append(Imaginaries())
		if '[' in right_cmd:
			# parse expression + matrix
			self.arglist.append(Matrix(left_cmd, right_cmd))
		else :
			arg = self.evaluator.ft_eval_brackets(right_cmd)
			arg.name = left_cmd
			self.arglist.append(arg)
		return 0

	def parse_eval(self, cmd: str) -> int:
		left_cmd = cmd.split('=')[0]
		# check matching brackets
		print(str(self.evaluator.ft_eval_brackets(self.formater.format_expression(left_cmd))))
		return 0
		if ('(' in left_cmd and ')' not in left_cmd) or (')' in left_cmd and '(' not in left_cmd):
			self.error_function(2)
		# if left_cmd function => check if function exists, eval f(x)
		# Better but could be upgraded
		name_func = left_cmd.split('(', 1)[0]
		func = None 
		if name_func is not None:
			for i in self.functions:
				if i.name == name_func:
					func = i
			if func is None:
				return(self.error_function(6))
		if func is not None:
			is_var = False
			var = left_cmd.split('(')[1].split(')')[0].strip()
			for i in self.arglist:
				if i.name == var:
					is_var = True
			if var is func.arg and is_var is False:
				print(f"{func.name}({var}) = ", func.expression)
				return 0
			elif self.isnumeric(var) is False and is_var is False:
				return(self.error_function(5))
			else:
				var = self.evaluator.ft_eval_brackets(var)
				print(f"{func.name}({var}) = ", self.evaluator.ft_eval_brackets(func.image(var))) 
		# if left_cmd var => eval left
		else:
			print(str(self.evaluator.ft_eval_brackets(self.formater.format_expression(left_cmd))))
		return 0

	def parse(self, cmd: str) -> int:
		cmd = cmd.lower()
		# check if no forbidden chars
		for char in cmd:
			if (char < 'a' or char > 'z') and (char < '0' or char > '9') \
				and char not in {'*', '/', '+', '=', '-', '^', '(', ')', '[', ']', ';', ',', ' ', '?', '.', '%'}:
				return(Error(1))
		if cmd == 'quit':
			return 0
		if '=' in cmd and '?' in cmd: # calculation
			return(self.parse_eval(cmd))
		if '=' in cmd and '?' not in cmd: # assignation
			left_cmd = cmd.split("=")[0].strip()
			right_cmd = cmd.split("=")[1].strip()
			if '(' in left_cmd or ')' in left_cmd:
				return(self.parse_function(left_cmd, right_cmd))
			else :
				# reduce right expression : real +/- i * img 
				return(self.parse_variable(left_cmd, right_cmd))#str(self.evaluator.ft_eval_brackets(right_cmd))))
		return 0

	@staticmethod
	def isnumeric(str):
		is_num = True
		for i in str:
			if not('0' <= i <= '9'):
				is_num = False
		return is_num

	@staticmethod
	def isfloat(value):
		try:
			float(value)
			return True
		except ValueError:
			return False