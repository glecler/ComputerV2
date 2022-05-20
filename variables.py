from __future__ import annotations
from error import Error

class Polynome():
    def __init__():
        pass
    
class Reals :
    def __init__(self, name : str, input : float) -> None :
        self.real = input
        self.name = name

    def __add__(self, other) :
        if type(other) is Error or type(other) is Matrix :
            return NotImplemented
        real = self.real + other.real
        if type(other) is Imaginaries :
            return Imaginaries('sum', real, other.img)
        return Reals('sum', real)

    def __radd__(self, other) :
        if type(other) is Error or type(other) is Matrix:
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
        if type(other) is Matrix :
            return NotImplemented
        if type(other) is Error :
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
        if type(other) is Matrix :
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
        if type(other) is Reals :
            real = self.real * other.real
            img = self.img * other.real
        if type(other) is Imaginaries :
            real = self.real * other.real - self.img * other.img 
            img = other.img * self.real + other.real * self.img
            return Imaginaries('rmul', real, img)
        return Imaginaries('rmul', real, img)
    
    def __pow__(self, other) :
        return NotImplemented

    def __mod__(self, other) :
        return Error(10)

    def __rmod__(self, other) :
        return Error(10)

    def __repr__(self) :
        return f'[{self.real} , {self.img}]'

    def __str__(self) :
        img_part = f'i * {self.img}' if self.img != 1 else f'i'
        real_part = f'{self.real} + ' if self.real != 0 else ''
        return real_part + img_part
    
    def copy(self) :
        return Imaginaries('', self.real, self.img)


class Matrix :

    def __init__(self, name, input) -> None:
        self.mat = list()
        self.name = name
        self.input = input
        rows = input.split(';')
        for i in range(len(rows)) :
            rows[i] = rows[i].strip().strip(']').strip('[').split(',')
            for j in range(len(rows[i])) :
                rows[i][j] = float(rows[i][j])
            self.mat.append(rows[i])
        self.check_rows()
        self.row_len = len(self.mat[0])
        self.col_len = len(self.mat)

    def __add__(self, other) :
        if type(other) is not Matrix :
            return NotImplemented
        if self.row_len != other.row_len or self.col_len != other.col_len :
            return Error(22)
        add_mat = self.copy()
        for i in range(len(self.mat)) :
            for j in range(len(self.mat[i])) :
                add_mat.mat[i][j] = self.mat[i][j] + other.mat[i][j]
        return add_mat
    
    def __radd__(self, other) :
        if type(other) is Matrix :
            return self + other
        return NotImplemented

    def __sub__(self, other) :
        if type(other) is Matrix : 
            return self + (other * -1)
        return NotImplemented
    
    def __rsub__(self, other) :
        return Error(13)
    
    def __pow__(self, other) :
        return Error(13)
    
    def __rpow__(self, other) :
        return Error(13)

    def __mul__(self, other) :
        mul_mat = []
        if type(other) is Reals :
            real = other.real
        if type(other) is (float or int) :
            real = other
        buff = '['
        for i in self.mat :
            buff += '['
            for j in i :
                j *= real
                buff += str(j) + ','
            buff = buff[:-1]
            buff += '];'
        buff = buff[:-1]
        buff += ']'
        return Matrix('', buff) 

    def __rmul__(self, other) :
        mul_mat = []
        print(type(other))
        print(other)
        if type(other) is Reals :
            real = other.real
        if type(other) is (float or int) :
            print(other)
            real = other
        buff = '['
        for i in self.mat :
            buff += '['
            for j in i:
                j *= real
                buff += str(j) + ','
            buff = buff[:-1]
            buff += '];'
        buff = buff[:-1]
        buff += ']'
        return(Matrix('', buff)) 

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
        return Matrix('', self.input)

    def check_rows(self) :
        row_len = len(self.mat[0])
        for row in self.mat :
            if len(row) != row_len :
                return(Error())



