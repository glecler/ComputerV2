class Formater():
	
	#def __init__(self, expression):
	#	self.exp = self.format_expression(expression)

	@staticmethod
	def format_expression(expression: str) -> str:
		output = ''
		print_nb = 0
		i = 0
		input = "".join(expression.split())
		while i < len(input):
		    try :
		        while (input[i] >= '0' and input[i] <= '9') or (input[i] >= 'a' and input[i] <= 'z') \
		            or (input[i] == '(' or input[i] == ')' or input[i] == '^' or input[i] == '.'):
		            output = output + input[i]
		            i += 1
		            print_nb = 1
		    except Exception: 
		        return(output)
		    if input[i] == '-' and  print_nb == 1:
		        output += ' - '
		    if input[i] == '-' and print_nb == 0:
		        output += ' -'
		    if input[i] == '*' or input[i] == '/' or input[i] == '%' or input[i] == '+':
		        output += ' ' + input[i] + ' '
		        print_nb = 0
		    i += 1
		return output