from __future__ import annotations
from function import *
from evaluator import *

class Graph:
	def __init__(self, arglist, funlist) :
		self.evaluator = Evaluator(arglist, funlist)

	def graph_min_max(self, fun : function, xmin : int, xmax : int) :
		#range = max - min
		step = ((xmax - xmin) // 40)
		popped = 0
		img_list = [self.evaluator.ft_eval(fun.image(i)).real if type(self.evaluator.ft_eval(fun.image(i))) == Rationnals else 0 for i in range(xmin, xmax, step)]
		print(img_list)
		img_max = max(img_list)
		minimum = min(img_list) - 1 
		count = len(img_list)
		mid = count // 2
		while max(img_list) != min(img_list) :
			print_buff = []
			count -= 1
			if count == mid :
				for i in range(xmin, xmax, step) :
					print('-', end='')
				print('\n')
			img_max = max(img_list)
			for i in range(len(img_list)) :
				if img_list[i] >= img_max : 
					print_buff.append(i)
			for i in range(xmin, xmax, step) :
				if (i + (xmax - xmin)//2) in print_buff :
					print('*', end='')
					img_list[i+(xmax-xmin)//2] = minimum
					popped += 1
				elif i == 0 :
					print('|', end='')
				else :
					print(' ', end='')
			print('\n')
		return img_list