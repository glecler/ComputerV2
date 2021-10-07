class Error:

	def __init__(self, error_code: int):
		self.err_code = error_code
		match error_code:
			case 1:
				self.err_msg = 'Unexpected character.'
			case 2:
				self.err_msg = 'Error : function format unreadable.\nExample format : \'f(x) = 2 * x + 3\''
			case 3:
				self.err_msg = 'Unknow function.'
			case 4:
				self.err_msg = 'Variable already exists.'
			case 5:
				self.err_msg = 'Variable does not exist.'
			case 6:
				self.err_msg = 'Function does not exist'
			case 7:
				self.err_msg = 'Function unknown.'
			case 8:
				self.err_msg = 'Parenthesis missing.'
			case 9:
				self.err_msg = 'Variable unknown.'
			case _:
				self.err_msg = 'Parsing error.'
	
	def __add__(self, other):
		return Error(self.err_code)

	def __sub__(self, other):
		return Error(self.err_code)

	def __rsub__(self, other):
		return Error(self.err_code)

	def __mul__(self, other):
		return Error(self.err_code)

	def __rmul__(self, other):
		return Error(self.err_code)

	def __str__(self):
		return(f"{self.err_msg}")