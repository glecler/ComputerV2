from variables import *

class Error :

	def __init__(self, error_code : int) :
		self.err_code = error_code
		match error_code :
			case 1 :
				self.err_msg = 'Unexpected character.'
			case 2 :
				self.err_msg = 'Function name format unreadable.'
			case 3 :
				self.err_msg = 'Unknow function.'
			case 4 :
				self.err_msg = 'Variable already exists.'
			case 5 :
				self.err_msg = 'Variable does not exist.'
			case 6 : 
				self.err_msg = 'Function does not exist'
			case 7 :
				self.err_msg = 'Function unknown.'
			case 8 :
				self.err_msg = 'Parenthesis missing.'
			case 9 :
				self.err_msg = 'Variable unknown.'
			case 10 :
				self.err_msg = 'Mod operator not supported for Complex number.'
			case 11 :
				self.err_msg = 'Can not divide by 0.'
			case 12 :
				self.err_msg = 'i can not be used as a variable.'
			case 13 :
				self.err_msg = 'Operation not permitted'
			case 14 :
				self.err_msg = 'Missing argument.'
			case 15 :
				self.err_msg = 'Too many \'=\' signs.'
			case 16 :
				self.err_msg = 'Non-real argument.'
			case 17 :
				self.err_msg = 'Variables can only be alpha.'
			case 18 :
				self.err_msg = 'Bracket missing.'
			case 19 :
				self.err_msg = 'Can not assign function to variable'
			case 20 :
				self.err_msg = 'Double characater.'
			case 21 :
				self.err_msg = 'Bad function format.'
			case _ :
				self.err_msg = 'Parsing error.'
	
	def __add__(self, other) :
		return Error(self.err_code)

	def __radd__(self, other) :
		return Error(self.err_code)
	
	def __pow__(self, other) :
		return Error(self.err_code)

	def __rpow__(self, other) :
		return Error(self.err_code)

	def __truediv__(self, other) :
		return Error(self.err_code)

	def __rtruediv__(self, other) :
		return Error(self.err_code)

	def __div__(self, other) :
		return Error(self.err_code)

	def __rdiv__(self, other) :
		return Error(self.err_code)

	def __sub__(self, other) :
		return Error(self.err_code)

	def __rsub__(self, other) :
		return Error(self.err_code)

	def __mul__(self, other) :
		return Error(self.err_code)

	def __rmul__(self, other) :
		return Error(self.err_code)

	def __str__(self) :
		return f'Error : {self.err_msg}\n'
	
	def copy(self) :
		return Error(self.err_code)
	
class SilentError(Error) :
	def __str__(self) :
		return ''