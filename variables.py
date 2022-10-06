from __future__ import annotations
from error import Error


class Variable :
    pass
# function should inherit variable, and polynome should inherit function

class Polynome :
    
    def __init__(self, variables) : # variables are any variable
        self.variables = variables
        self.varBuff = []
        print("varibales should be set", self.variables)
        if True in [True if type(i) == Polynome else False for i in self.variables ] :
            self.reduce_polynome()
        #TODO sort coeffs
    
    # variables constructing Polynome can themselves be of type Polynome
    # this simple function reduces the variables to Unknown by distibuting additively the Polynomes in variables
    # note : if this is done every time a polynome is instancianted, there should not be nested Polynomes in the variables

    def reduce_polynome(self) :
        varBuff = []
        retBuff = []


        for var in self.variables :
            if type(var) is not Polynome :
                varBuff.append(var)
            else :
                for subVar in var :
                    varBuff.append(subVar)
        seenDegrees = []
        for i in varBuff :
            if type(i) == int:
                return
        for var in varBuff :
            if var.degree not in seenDegrees :
                retBuff.append(sum([retVar for retVar in varBuff if var.degree == retVar.degree]))
                seenDegrees.append(var.degree)
        self.variables = retBuff

    # x^2 + 2*x - 2 * x^2 + 3*x
    # x + 2 * x
    # we consider that self and other are properly reduced
    def __add__(self, other):
        varBuff = []
        if type(other) is Polynome :
            for i in self.variables :
                for j in other.variables :
                    if i.degree == j.degree :
                        varBuff.append(i + j)
            return Polynome(varBuff)
        done = False
        for i in self.variables :
            j = i
            if other.degree == i.degree :
                j = i + other
                done = True
            varBuff.append(j)
        if done == False :
            varBuff.append(other)
        return Polynome(varBuff)
    
    def __radd__(self, other):
        self.__add__(other)

    def __mul__(self, other):
        if type(other) == Reals or type(other) == Unknown :
            print(Polynome([i * other for i in self.variables]))
            return Polynome([i * other for i in self.variables])

    def __rmul__(self, other):
        if type(other) == Reals or type(other) == Unknown :
            print(Polynome([i * other for i in self.variables]))
            return Polynome([i * other for i in self.variables])

    def __repr__(self) :
        # {{a, b, c}} 
        buff = ''
        for i in self.variables :
            buff += repr(i) + ';'
        buff = buff[:-1]
        return '{{' + f'{buff}' + '}}'
    
    def __str__(self) :
        varBuff = ''
        count = 0
        print("??", self.variables)
        for i in self.variables :
            varBuff += (' + ' if i.coefficient >= 0 and count > 0 else ' - ' if count > 0 else '') + str(i)
            count += 1
        return varBuff

class Unknown :
    def __init__(self, name, coefficient, degree) -> None :      # coefficient are any variable except Unknown, degree are Reals
        self.name = name
        self.coefficient = coefficient
        self.degree = degree

    def __add__(self, other) : # 3 * a + a
        if type(other) is Unknown :
            if other.name == self.name and other.degree == self.degree :
                return Unknown(self.name, self.coefficient + other.coefficient, self.degree)  # error management if coeff type operation not possible?
        return Polynome([other, self])

    def __radd__(self, other) : # 3 * a + a
        if type(other) is Unknown :
            if other.name == self.name and other.degree == self.degree :
                return Unknown(self.name, self.coefficient + other.coefficient, self.degree)  # error management if coeff type operation not possible?

        return Polynome([other, self])

    def __sub__(self, other) : #
        if type(other) is Unknown :
            if other.name == self.name and other.degree == self.degree :
                return Unknown(self.name, self.coefficient - other.coefficient, self.degree)
    
    def __mul__(self, other):
        if type(other) == Polynome : 
            return NotImplemented
        if type(other) is Reals:
            return Unknown(self.name, self.coefficient * other.real, self.degree)
        if type(other) is Unknown and self.name == other.name :
            return Unknown(self.name, self.coefficient * other.coefficient, self.degree + other.degree)

    def __rmul__(self, other):
        if type(other) == Polynome : 
            return NotImplemented
        if type(other) is Reals:
            return Unknown(self.name, self.coefficient * other.real, self.degree)
        if type(other) is Unknown and self.name == other.name :
            return Unknown(self.name, self.coefficient * other.coefficient, self.degree + other.degree)
    
    def __repr__(self):
        return f'<{self.name},{self.coefficient},{self.degree}>'

    def __str__(self):
        return (f'{self.coefficient} * ' if self.coefficient > 1 else '') + f'{self.name}' + (f'^{self.degree}' if self.degree > 1 else '')
    
class Reals :
    def __init__(self, name : str, input : float) -> None :
        self.real = input
        self.name = name
        self.degree = 0
        self.coefficient = self.real

    def __add__(self, other) :
        if type(other) is int:
            return Reals('', self.real + other)
        if other == None or type(other) is Error or type(other) is Matrix or type(other) is Unknown :
            return NotImplemented
        real = self.real + other.real
        if type(other) is Imaginaries :
            return Imaginaries('sum', real, other.img)
        return Reals('sum', real)

    def __radd__(self, other) :
        if type(other) is int:
            return Reals('', self.real + other)
        if type(other) is Error or type(other) is  Matrix or type(other) is  Unknown:
            return NotImplemented
        real = self.real + other.real
        if type(other) is Imaginaries :
            return Imaginaries('sum', real, other.img)
        return Reals('sum', real)

    def __sub__(self, other) :
        if type(other) is Error :
            return NotImplemented
        real = self.real - other.real
        if type(other) is Imaginaries :
            return Imaginaries('sum', real, -other.img)
        return Reals('sum', real)
    
    def __rsub__(self, other) :
        if type(other) is Error :
            return NotImplemented
        real = other.real - self.real
        if type(other) is Imaginaries :
            return Imaginaries('sum', real, other.img)
        return Reals('sum', real)
    
    def __rmul__(self, other) :
        if type(other) == Matrix or type(other) == Unknown or type(other) == Polynome :
            return NotImplemented
        if type(other) == Error :
            return Error(other.err_code)
        real = 0
        img = 0
        if type(other) is Reals :
            real = self.real * other.real
        if type(other) is Imaginaries :
            real = self.real * other.real
            img = other.img * self.real
            return Imaginaries('rmul', real, img)
        return Reals('rmul', real)
    
    def __mul__(self, other) :
        if type(other) == Matrix or type(other) == Unknown or type(other) == Polynome :
            return NotImplemented
        if type(other) is Error :
            return Error(other.err_code)
        real, img = 0, 0
        if type(other) is Reals :
            real = self.real * other.real
        if type(other) is Imaginaries :
            real = self.real * other.real
            img = other.img * self.real
            return Imaginaries('mul', real, img)
        return Reals('mul', real)

    def __truediv__(self, other) :
        if type(other) is Error :
            return NotImplemented
        if type(other) is (float or int) and other != 0 :
            return Reals('', self.real/other)
        elif type(other) is (float or int) and other == 0 :
            return Error(11) 
        if type(other) is Reals and other.real != 0 :
            return Reals('', self.real / other.real)
        if type(other) is Reals and other.real == 0 :
            return Error(11)
        if type(other) is Imaginaries :
            return NotImplemented
        return self
        
    def __rtruediv__(self, other) :
        if type(other) is Error :
            return NotImplemented
        if type(other) is (float or int) and other != 0 :
            return Reals('',other/self.real)
        elif type(other) is (float or int) and other == 0 :
            return Error(11)
        if type(other) is Reals and self.real == 0 :
            return Error(11)
        if type(other) is Reals and self.real != 0 :
            return Reals('',other.real / self.real)
        return self
    
    def __mod__(self, other) :
        if type(other) is Error :
            return NotImplemented
        if type(other) is (float or int) and other != 0 :
            return Reals('', self.real % other)
        elif type(other) is (float or int) and other == 0 :
            return Error(11)
        if type(other) is Reals :
            return Reals('', self.real % other.real)
        if type(other) is Imaginaries :
            return NotImplemented
    
    def __pow__(self, other) :
        if type(other) is (Error or Imaginaries) :
            return NotImplemented
        if type(other) is (int or float) :
            return Reals('', pow(self.real, other))
        if type(other) is Reals :
            return Reals('', pow(self.real, other.real))
    
    def __str__(self) :
        return(f'{self.real}')
    
    def __repr__(self) :
        return(f'{self.real}')
    
    def copy(self) :
        return Reals('', self.real)


class Imaginaries :
    def __init__(self, name : str, realpart : float, imgpart : float) -> None:
        self.name = name
        self.real = realpart
        self.img = imgpart
    
    def __add__(self, other) :
        if type(other) is Error :
            return NotImplemented
        real = self.real + other.real
        img = self.img + other.img \
            if type(other) is Imaginaries else self.img
        return Imaginaries('', real, img)

    def __sub__(self, other) :
        if type(other) is Error :
            return NotImplemented
        real = self.real - other.real
        img = self.img - other.img \
            if type(other) is Imaginaries else self.img
        return Imaginaries('', real, img)
    
    def __rsub__(self, other) :
        if type(other) is Error :
            return NotImplemented
        real = other.real - self.real
        img = other.img - self.img \
            if type(other) is Imaginaries else -self.img
        return Imaginaries('', real, img)

    def __truediv__(self, other) :
        if type(other) is Error :
            return NotImplemented
        if type(other) is (float or int) and other != 0 :
            return Imaginaries('', self.real / other, self.img / other)
        elif type(other) is (float or int) and other == 0 :
            return Error(11)
        if type(other) is Reals :
            return Imaginaries('', self.real / other.real, self.img / other.real)
        if type(other) is Imaginaries :
            return Imaginaries('', (self.real * other.real + other.img * self.img) / (other.real**2 + other.img**2), \
                (other.real * self.img - self.real * other.img) / (other.real**2 + other.img**2))
        return self
        
    def __rtruediv__(self, other) :
        if type(other) is Error :
            return NotImplemented
        if type(other) is (float or int) and other != 0 :
            return Imaginaries('', other * self.real / (self.real**2 + self.img**2),\
                -other * self.img / (self.real**2 + self.img**2))
        elif type(other) is (float or int) and other == 0 :
            return Error(11)
        if type(other) is Reals :
            return Imaginaries('', other.real * self.real / (self.real**2 + self.img**2), \
                -other.real * self.img / (self.real**2 + self.img**2))
        if type(other) is Imaginaries :
            return Imaginaries('', (other.real * self.real + self.img * other.img) / (self.real**2 + self.img**2), \
                (self.real * other.img - other.real * self.img) / (self.real**2 + self.img**2))
        return self

    def __rmul__(self, other) :
        if type(other) is Error :
            return NotImplemented
        real = 0
        img = 0
        if type(other) is Reals :
            real = self.real * other.real
            img = self.img * other.real
        if type(other) is Imaginaries :
            real = other.real * self.real - other.img * self.img 
            img = other.img * self.real + other.real * self.img
            return Imaginaries('rmul', real, img)
        return Imaginaries('rmul', real, img)
    
    def __mul__(self, other) :
        if type(other) is Error :
            return NotImplemented
        real = 0
        img = 0
        if type(other) is int:
            real = self.real * other
            img = self.img * other
        if type(other) is Reals:
            real = self.real * other.real
            img = self.img * other.real
        if type(other) is Imaginaries :
            real = self.real * other.real - self.img * other.img 
            img = other.img * self.real + other.real * self.img
            return Imaginaries('rmul', real, img)
        return Imaginaries('rmul', real, img)
    
    def __pow__(self, other) :
        if type(other) is int or Reals:
            if type(other) is Reals :
                other = other.real
            if other == 0 :
                return 1
            ret = 1
            for i in range(int(other)) :
                ret = self * ret
            return ret
        return NotImplemented

    def __mod__(self, other) :
        return Error(10)

    def __rmod__(self, other) :
        return Error(10)

    def __repr__(self) :
        return f'[{self.real} , {self.img}]'

    def __str__(self) :
        img_part = f'{self.img}i' if self.img != 1 else f'i'
        real_part = f'{self.real}' if self.real != 0 else ''
        return real_part + ('+' if  (self.img > 0 and real_part != '') else '-' if self.img < 0 else '') + (img_part if  self.img != 0 else '')
    
    def copy(self) :
        return Imaginaries('', self.real, self.img)


class Matrix :

    def __init__(self, name, mat) -> None:
        self.mat = mat
        self.name = name
        self.check_rows()
        self.row_len = len(self.mat)
        self.col_len = len(self.mat[0])

    def __add__(self, other) :
        if type(other) is not Matrix :
            return NotImplemented
        if self.row_len != other.row_len or self.col_len != other.col_len :
            return Error(22)
        add_mat = [] # self.copy()
        for i in range(len(self.mat)) :
            add_mat.append([])
            for j in range(len(self.mat[i])) :
                add_mat[i].append(self.mat[i][j] + other.mat[i][j])
        return Matrix('', add_mat)
    
    def __radd__(self, other) :
        if type(other) is Matrix :
            return self + other
        return NotImplemented

    def __sub__(self, other) :
        if type(other) is not Matrix :
            return NotImplemented
        if self.row_len != other.row_len or self.col_len != other.col_len :
            return Error(22)
        sub_mat = self.copy()
        for i in range(len(self.mat)) :
            for j in range(len(self.mat[i])) :
                sub_mat.mat[i][j] = self.mat[i][j] - other.mat[i][j]
        return sub_mat

    def __rsub__(self, other) :
        return Error(13)
    
    def __pow__(self, other) :
        if type(other) is not Matrix :
            return NotImplemented
        mul_mat = []
        for i in range(other.row_len) :
            mul_mat.append([])
            for j in range(self.col_len) :
                mul_mat[i].append(sum([x * y[i] for x in self.mat[j] for y  in other.mat]))
        return Matrix('', mul_mat)
        
    
    def __rpow__(self, other) :
        return Error(13)

    def __mul__(self, other) :
        if type(other) is Matrix :
            return NotImplemented
        mul_mat = self.copy()
        if type(other) is Reals :
            real = other.real
        if type(other) is (float or int) :
            real = other
        for i in range(len(self.mat)) :
            for j in range(len(self.mat[i])) :
                mul_mat.mat[i][j] *= real
        return Matrix('', mul_mat.mat) 

    def __rmul__(self, other) :
        mul_mat = self.copy()
        if type(other) is Reals :
            real = other.real
        if type(other) is (float or int) :
            real = other
        for i in range(len(self.mat)) :
            for j in range(len(self.mat[i])) :
                mul_mat.mat[i][j] *= real
        return(Matrix('', mul_mat.mat)) 

    def __str__(self) :
        buff = ''
        for i in self.mat :
            buff += str(i) + '\n'
        buff = buff[:-1]
        return f'{buff}'

    def __repr__(self) :
        buff = '['
        for i in self.mat :
            buff += str(i)
            buff += ';'
        buff = buff[:-1]
        buff += ']'
        return f'{buff}'

    def copy(self) :
        return Matrix('', self.mat)

    def check_rows(self) :
        row_len = len(self.mat[0])
        for row in self.mat :
            if len(row) != row_len :
                return(Error())



