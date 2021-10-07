from __future__ import annotations
from error import Error

class Variable:
	def __init__(self) -> None:
		pass

class Unknown(Variable):
	def __init__(self, name: str) -> None:
		self.name = name.strip()
	
	def __add__(self, other):
		name = self.name + ' + ' + str(other)
		return Unknown(name)

	def __sub__(self, other):
		name = self.name + ' - ' + str(other)
		return Unknown(name)

	def __rsub__(self, other):
		name = str(other) + ' - ' + self.name
		return Unknown(name)

	def __mul__(self, other):
		name = self.name + ' * ' + str(other)
		return Unknown(name)
	
	def __rmul__(self, other):
		name = self.name + ' * ' + str(other)
		return Unknown(name)
	
	#def __div__(self, toher)
	def __repr__(self):
		return(f"{self.name}")

	def __str__(self):
		return(f"{self.name}")

class Rationnals(Variable):
	def __init__(self, name: str, input: float) -> None:
		self.real = input
		self.name = name

	def __add__(self, other: Rationnals) -> Rationnals | Imaginaries:
		if type(other) is Error:
			return NotImplemented
		if type(other) is Unknown:
			return other + self
		real = self.real + other.real
		if type(other) is Imaginaries:
			return Imaginaries("sum", real, other.img)
		return Rationnals("sum", real)

	def __sub__(self, other: Rationnals) -> Rationnals | Imaginaries:
		if type(other) is Error:
			return NotImplemented
		if type(other) is Unknown:
			return NotImplemented
		real = self.real - other.real
		if type(other) is Imaginaries:
			return Imaginaries("sum", real, -other.img)
		return Rationnals("sum", real)
	
	def __rsub__(self, other: Rationnals) -> Rationnals | Imaginaries:
		if type(other) is Error:
			return NotImplemented
		if type(other) is Unknown:
			return other - self
		real = other.real - self.real
		if type(other) is Imaginaries:
			return Imaginaries("sum", real, other.img)
		return Rationnals("sum", real)
	
	def __rmul__(self, other) -> Rationnals:
		if type(other) is Error:
			return NotImplemented
		real = 0
		img = 0
		if type(other) is Unknown:
			return other * self
		if (type(other) is Rationnals):
			real = self.real * other.real
		if type(other) is Imaginaries:
			real = self.real * other.real
			img = other.img * self.real
			return Imaginaries("rmul", real, img)
		return Rationnals("rmul", real)
	
	def __mul__(self, other) -> Rationnals:
		if type(other) is Error:
			return NotImplemented
		real = 0
		img = 0
		if type(other) is Unknown:
			return other * self
		if type(other) is Rationnals:
			real = self.real * other.real
		if type(other) is Imaginaries:
			real = self.real * other.real
			img = other.img * self.real
			return Imaginaries("mul", real, img)
		return Rationnals("mul", real)

	def __str__(self):
		return(f"{self.real}")
	
	def __repr__(self):
		return(f"{self.real}")


class Imaginaries(Variable):
	def __init__(self, name: str, realpart: float, imgpart: float) -> None:
		self.name = name
		self.real = realpart
		self.img = imgpart
	
	def __add__(self, other: Imaginaries | Rationnals) -> Imaginaries:
		if type(other) is Error:
			return NotImplemented
		name = "sum"
		real = self.real + other.real
		if type(other) is Imaginaries:
			img = self.img + other.img
		else:
			img = self.img
		return Imaginaries(name, real, img)

	def __sub__(self, other):
		if type(other) is Error:
			return NotImplemented
		name = "sub"		
		real = self.real - other.real
		if type(other) is Imaginaries:
			img = self.img - other.img
		else:
			img = self.img
		return Imaginaries(name, real, img)
	
	def __rsub__(self, other):
		if type(other) is Error:
			return NotImplemented
		name = "sub"
		real = other.real - self.real
		if type(other) is Imaginaries:
			img = other.img - self.img
		else:
			img = -self.img
		return Imaginaries(name, real, img)

	def __rmul__(self, other) -> Rationnals:
		if type(other) is Error:
			return NotImplemented
		real = 0
		img = 0
		if type(other) is Rationnals:
			real = self.real * other.real
			img = self.img * other.real
		if type(other) is Imaginaries:
			real = other.real * self.real - other.img * self.img 
			img = other.img * self.real + other.real * self.img
			return Imaginaries("rmul", real, img)
		return Imaginaries("rmul", real, img)
	
	def __mul__(self, other) -> Rationnals:
		if type(other) is Error:
			return NotImplemented
		real = 0
		img = 0
		if type(other) is Rationnals:
			real = self.real * other.real
			img = self.img * other.real
		if type(other) is Imaginaries:
			real = self.real * other.real - self.img * other.img 
			img = other.img * self.real + other.real * self.img
			return Imaginaries("rmul", real, img)
		return Imaginaries("rmul", real, img)

	def __repr__(self):
		return(f"[{self.real} , {self.img}]")

	def __str__(self):
		return(f"{self.real} + i * {self.img}")


class Matrix(Variable):
	#check format matrix
	def __init__(self, name, input) -> None:
		self.mat = list()
		self.name = name
		rows = input.split(";")
		for i in range(len(rows)):
			rows[i] = rows[i].strip("]").strip("[").split(',')[0], rows[i].strip("]").strip("[").split(',')[1]
			self.mat.append(rows[i])
		print(self.mat)
	
#img = Imaginaries("A", 2, 2)
#reel = Rationnals("B", 4)
#if issubclass(type(img), Variable):
#	print(img)
#print(reel+reel)
#print(img+reel) # img
#print(reel+img) # reel