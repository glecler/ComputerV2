from interpreter import Interpreter
from error import Error

def test_main():
    interpreter  = Interpreter()
    error = Error(0)
    assert str(interpreter.parse('a = 0')) == '0.0'
    assert type(interpreter.parse('x == 2')) == type(error)
    assert 2==2
