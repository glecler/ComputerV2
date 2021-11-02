#!/usr/bin/python3
from typing import Optional
from function import *
from variables import *
from evaluator import *
from formater import Formater
from error import Error
from graph import *

class Interpreter:
	
	def __init__(self) :
		self.functions = []
		self.arglist = []
		self.history = []
		self.arglist.append(Imaginaries('i', 0, 1))
		self.functions.append(Cosinus('cos(x)', 'cos(x)'))
		self.functions.append(Sinus('sin(x)', 'sin(x)'))
		self.evaluator = Evaluator(self.arglist, self.functions)
		self.formater = Formater()
		self.graph = Graph(self.arglist, self.functions)
	
	def check_fun_format(self, function : str) :
		pass
	
	def check_fun_name_format(self, function : str) -> bool :
		var = ''
		if ' ' in function :
			return False
		i = 0
		while function[i] >= 'a' and function[i] <= 'z' :
			var += function[i]
			i += 1
		if function[i] == '(' :
			i += 1
			while function[i] >= 'a'and function[i] <= 'z' :
				i += 1
		if function[i] == ')' :
			return True
		return False

	# check function format f(x) = something
	# assign formated expression
	# check right member validity = only numerical + matrix + functions + arg of function
	def parse_function(self, left_cmd : str, right_cmd : str) -> int :
		if not self.check_fun_name_format(left_cmd) :
			return Error(2)
		#if not self.check_fun_format(right_cmd) :
		#	return Error(21)
		exp = self.formater.format_expression(right_cmd, self.functions).split()
		x_arg = left_cmd.split('(')[1].split(')')[0]
		for i in range(len(exp)) :
			for arg in self.arglist :
				if exp[i] == arg.name and exp[i] != x_arg :
					exp[i] = str(arg)
		input = self.formater.format_expression(''.join(exp), self.functions)
		# TODO check right cmd input
		for i in range(len(self.functions)) :
			if self.functions[i].name == left_cmd.split('(')[0] :
				self.functions[i] = Function(left_cmd, input)
				return self.functions[i]
		self.functions.append(Function(left_cmd, input))
		return self.functions[-1]
	
	# variables here : R, C, matrix
	# check left member only alpha and not i
	# eval right member and assign to left member
	# if left member not already a variable, append, else reassign
	def parse_variable(self, left_cmd : str, right_cmd : str) :	
		for i in left_cmd :
			if i > 'z' or i < 'a' :
				return Error(17)
		if left_cmd.strip() == 'i' :
			return Error(12)
		for i in range(len(self.arglist)) :
			if self.arglist[i].name == left_cmd and \
				type(self.evaluator.ft_eval(right_cmd)) not in {SilentError, Error} :   # reassign variable
				self.arglist[i] = self.evaluator.ft_eval(right_cmd)
				self.arglist[i].name = left_cmd
				return self.arglist[i]
		if arg := self.evaluator.ft_eval(right_cmd) :									# append new variable
			arg.name = left_cmd
			if type(arg) is SilentError :
				return Error(19)
			if type(arg) not in {SilentError, Error} :
				self.arglist.append(arg)
			return arg
		else :
			return Error(0)

	def parse_eval(self, cmd : str) :
		if cmd.split('=')[1].strip() != '?' :
			pass
			# TODO : equations
		exp = self.formater.format_expression(cmd.split('=')[0], self.functions).replace('-', '-1*')
		return self.evaluator.ft_eval(exp)

	def ft_parse_commands(self, cmd : str) :
		match cmd :
			case 'quit' :
				return 0
			case 'var' :
				return [self.arglist[i].name for i in range(1, len(self.arglist))]
			case 'fun' :
				return [i.name for i in self.functions]
			case 'graph f(x)' :
				return self.graph.graph_min_max(self.functions[0], -20, 20)
			case 'history' :
				return self.history
	
	def ft_check_parsing(self, cmd : str) :
		if not self.iseven(cmd, '(', ')') :
			return Error(8)
		if not self.iseven(cmd, '[', ']') :
			return Error(18)
		if 0 != sum(1 for i in cmd if i == '=') != 1 :
			return Error(15)
		buff_char = ''
		for char in cmd :
			if char == buff_char and char in {'.', '/', '%', '+', ',', ';', '^'} :
				return Error(20)
			if (char < 'a' or char > 'z') and (char < '0' or char > '9') \
				and char not in {'*', '/', '+', '=', '-', '^', '(', ')', \
					'[', ']', ';', ',', ' ', '?', '.', '%'} :
				return Error(1)
			buff_char = char
		if cmd.split('=')[0].strip() == '' or cmd.split('=')[1].strip() == '' :
			return Error(14)
		return True
	
	def parse(self, cmd : str) :
		self.history.append('> ' + cmd)
		cmd = cmd.lower()
		if '=' not in cmd :
			if cmd == 'history' :
				return self.ft_parse_commands(cmd)
			cmd = self.ft_parse_commands(cmd)
			self.history.append(str(cmd))
			return cmd
		if type(err := self.ft_check_parsing(cmd)) == Error :
			self.history.append(err)
			return err
		if '?' in cmd : # calculation
			cmd = self.parse_eval(cmd)
			self.history.append(str(cmd))
			return cmd
		left_cmd = cmd.split('=')[0].strip()
		right_cmd = cmd.split('=')[1].strip()
		if '(' in left_cmd or ')' in left_cmd :
			cmd = self.parse_function(left_cmd, right_cmd)
			self.history.append(str(cmd))
			return cmd
		cmd = self.parse_variable(left_cmd, \
			self.formater.format_expression(right_cmd, self.functions))
		self.history.append(str(cmd))
		return cmd

	@staticmethod
	def iseven(cmd : str, char_right : str, char_left : str) :
		right_bracket = [True for l in cmd if l == char_right]
		left_bracket = [True for l in cmd if l == char_left]
		if len(right_bracket) != len(left_bracket) :
			return False
		return True
	
	@staticmethod
	def isnumeric(string : str) :
		is_num = True
		for i in string :
			if not('0' <= i <= '9') :
				is_num = False
		return is_num

	@staticmethod
	def isfloat(value) :
		try :
			float(value)
			return True
		except ValueError :
			return False