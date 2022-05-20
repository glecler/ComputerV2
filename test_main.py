from interpreter import *
import sys

class Colors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'
    OK = OKGREEN + '[OK]' + ENDC
    KO = FAIL + '[KO]' + ENDC

def prompt():
    cmd = input('> ')
    return(cmd)

def main():
    interpreter = Interpreter()
    colors = Colors
    print(colors.FAIL + '\n--------------------------\n' + colors.ENDC)
    print(colors.FAIL + '\n----------TEST-------------\n' + colors.ENDC)
    print(colors.FAIL + '\n----------MAIN------------\n' + colors.ENDC)
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)

    print(colors.OKBLUE + 'Partie Assignation' + colors.ENDC)
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)

    print(colors.OKBLUE + 'Test Erreur Elementaire'+ colors.ENDC + '\n')
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)

    print('> a = 0')
    print(interpreter.parse('a = 0'), colors.OK if str(interpreter.parse('a = 0')) == '0.0' else colors.KO)
    print('\n')

    print('> x == 2')
    print(interpreter.parse('x == 2'), colors.OK if type(interpreter.parse('x == 2')) == Error else colors.KO)
    print('\n')

    print('> x = 23edd23-+-+')
    print(interpreter.parse('x = 23edd23-+-+'), colors.OK if type(interpreter.parse('x = 23edd23-+-+')) == Error else colors.KO)
    print('\n')

    print('> var')
    print(interpreter.parse('var'))
    print('\n')
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)

    print(colors.OKBLUE + '\nTest Erreur Semi Avancé \n'+ colors.ENDC)
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)

    interpreter = Interpreter()
    print(interpreter.parse('var'))
    print('> = 2')
    print(interpreter.parse('= 2'), colors.OK if type(interpreter.parse('= 2')) == Error else colors.KO)
    print('\n')

    print('> 3 = 4')
    print(interpreter.parse('3 = 4'), colors.OK if type(interpreter.parse('3 = 4')) == Error else colors.KO)
    print('\n')

    print('> x = g')
    print(interpreter.parse('x = g'), colors.OK if type(interpreter.parse('x = g')) == Error else colors.KO)
    print('\n')

    print('> f(x = 2')
    print(interpreter.parse('f(x = 2'), colors.OK if type(interpreter.parse('f(x = 2')) == Error else colors.KO)
    print('\n')

    print('> x = [[4, 2]')
    print(interpreter.parse('x = [[4, 2]'), colors.OK if type(interpreter.parse('x = [[4, 2]')) == Error else colors.KO)
    print('\n')

    print('> var')
    print(interpreter.parse('var'))
    interpreter = Interpreter()
    print('\n')
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)

    print(colors.OKBLUE + '\nTest Erreur Avancé \n' + colors.ENDC)
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)
    
    print('> x = --2')
    print(interpreter.parse('x = --2'), colors.OK if str(interpreter.parse('x = --2')) == '2.0' else colors.KO)
    print('\n')

    print('> f(x) = x * 2')
    print(interpreter.parse('f(x) = x * 2'), colors.OK if str(interpreter.parse('f(x) = x * 2')) == 'x * 2' else colors.KO)
    print('\n')

    print('> t = f(x) ')
    print(interpreter.parse('t = f(x)'), colors.OK if type(interpreter.parse('t = f(x)')) == Error else colors.KO)
    print('\n')

    print('> i = 2')
    print(interpreter.parse('i = 2'), colors.OK if type(interpreter.parse('i = 2')) == Error else colors.KO)
    print('\n')

    print('> var')
    print(interpreter.parse('var'))
    print('\n')
    interpreter = Interpreter()
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)

    print(colors.OKBLUE + '\n Test Valide Élémentaire\n' + colors.ENDC)
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)

    print('> x = 2')
    print(interpreter.parse('x = 2'), colors.OK if str(interpreter.parse('x = 2')) == '2.0' else colors.KO)
    print('\n')
    
    print('> x = ?')
    print(interpreter.parse('x = ?'), colors.OK if str(interpreter.parse('x = ?')) == '2.0' else colors.KO)
    print('\n')

    print('> y = 4i')
    print(interpreter.parse('y = 4i'), colors.OK if str(interpreter.parse('y = 4i')) == 'i * 4.0' else colors.KO)
    print('\n')

    print('> y = ?')
    print(interpreter.parse('y = ?'), colors.OK if str(interpreter.parse('y = ?')) == 'i * 4.0' else colors.KO)
    print('\n')

    print('> z = [[2, 3];[3, 5]]')
    print(interpreter.parse('z = [[2, 3];[3, 5]]'), colors.OK if str(interpreter.parse('z = [[2, 3];[3, 5]]')) == str(Matrix('', '[[2, 3];[3, 5]]')) else colors.KO)
    print('\n')

    print('> z = ?')
    print(interpreter.parse('z = ?'), colors.OK if str(interpreter.parse('z = ?')) == str(Matrix('', '[[2, 3];[3, 5]]')) else colors.KO)
    print('\n')
    
    print('> var')
    print(interpreter.parse('var'))
    interpreter = Interpreter()
    print('\n')
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)

    print(colors.OKBLUE + '\nTest Valide Semi Avancé\n' + colors.ENDC)
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)
    
    print('> x = 2')
    print(interpreter.parse('x = 2'), colors.OK if str(interpreter.parse('x = 2')) == '2.0' else colors.KO)
    print('\n')

    print('> y = x')
    print(interpreter.parse('y = x'), colors.OK if str(interpreter.parse('y = x')) == '2.0' else colors.KO)
    print('\n')
    
    print('> y = ?')
    print(interpreter.parse('y = ?'), colors.OK if str(interpreter.parse('y = ?')) == '2.0' else colors.KO)
    print('\n')

    print('> x = 2')
    print(interpreter.parse('x = 2'), colors.OK if str(interpreter.parse('x = 2')) == '2.0' else colors.KO)
    print('\n')

    print('> x = 5')
    print(interpreter.parse('x = 5'), colors.OK if str(interpreter.parse('x = 5')) == '5.0' else colors.KO)
    print('\n')
    
    print('> x = ?')
    print(interpreter.parse('x = ?'), colors.OK if str(interpreter.parse('x = ?')) == '5.0' else colors.KO)
    print('\n')

    print('> A = [[2, 3]]')
    print(interpreter.parse('A = [[2, 3]]'), colors.OK if str(interpreter.parse('A = [[2, 3]]')) == str(Matrix('','[[2, 3]]')) else colors.KO)
    print('\n')

    print('> B = A')
    print(interpreter.parse('B = A'), colors.OK if str(interpreter.parse('B = A')) == str(Matrix('','[[2, 3]]')) else colors.KO)
    print('\n')

    print('> B = ?')
    print(interpreter.parse('B = ?'), colors.OK if str(interpreter.parse('B = ?')) == str(Matrix('','[[2, 3]]')) else colors.KO)
    print('\n')

    print('> var')
    print(interpreter.parse('var'))
    print('\n')

    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)
    print(colors.OKBLUE + '\nTest Valide Avancé\n' + colors.ENDC)
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)
    
    interpreter = Interpreter()
    print('> x = 2')
    print(interpreter.parse('x = 2'), colors.OK if str(interpreter.parse('x = 2')) == '2.0' else colors.KO)
    print('\n')

    print('> f(x) = x * 5')
    print(interpreter.parse('f(x) = x * 5'), colors.OK if str(interpreter.parse('f(x) = x * 5')) == 'x * 5' else colors.KO)
    print('\n')
    
    print('> f(x) = ?')
    print(interpreter.parse('f(x) = ?'), colors.OK if str(interpreter.parse('f(x) = ?')) == 'x * 5' else colors.KO)
    print('\n')

    print('> x = 2')
    print(interpreter.parse('x = 2'), colors.OK if str(interpreter.parse('x = 2')) == '2.0' else colors.KO)
    print('\n')
    
    print('> y = x * [[4, 2]]')
    print(interpreter.parse('y = x * [[4, 2]]'), colors.OK if str(interpreter.parse('y = x * [[4, 2]]')) == str(Matrix('','[[8, 4]]')) else colors.KO)
    print('\n')

    print('> var')
    print(interpreter.parse('var'))
    print('\n')
    print('> fun')
    print(interpreter.parse('fun'))
    print('\n')
    print('> history')
    print(interpreter.parse('history'))
    print('\n')


    print('> f(z) = z * y ')
    print(interpreter.parse('f(z) = z * y'), colors.OK if str(interpreter.parse('f(z) = z * y')) == 'z * [[8.0,4.0]]' else colors.KO)
    print('\n')
    
    print('> f(z) = ?')
    print(exp := str(interpreter.parse('f(z) = ?')), colors.OK if exp == 'z * [[8.0,4.0]]' else colors.KO)
    print('\n')

    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)
    print(colors.OKBLUE + '\nPartie calculatoire\n' + colors.ENDC)
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)
    print(colors.OKBLUE + '\nTest Valide Élémentaire\n' + colors.ENDC)
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)

    print('> 2 + 2 = ?')
    print(interpreter.parse('2 + 2 = ?'), colors.OK if str(interpreter.parse('2 + 2 = ?')) == '4.0' else colors.KO)
    print('\n')

    print('> 3 * 4 = ?')
    print(interpreter.parse('3 * 4 = ?'), colors.OK if str(interpreter.parse('3 * 4 = ?')) == '12.0' else colors.KO)
    print('\n')

    print('> x = 2')
    print(interpreter.parse('x = 2'), colors.OK if str(interpreter.parse('x = 2')) == '2.0' else colors.KO)
    print('\n')

    print('> x + 2 = ?')
    print(interpreter.parse('x + 2 = ?'), colors.OK if str(interpreter.parse('x + 2 = ?')) == '4.0' else colors.KO)
    print('\n')

    print('> 2/0= ?')
    print(interpreter.parse('2 / 0 = ?'), colors.OK if type(interpreter.parse('2 / 0 = ?')) == Error else colors.KO)
    print('\n')

    print('> 1.5 + 1 = ?')
    print(interpreter.parse('1.5 + 1 = ?'), colors.OK if str(interpreter.parse('1.5 + 1 = ?')) == '2.5' else colors.KO)

    print('\n')
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)
    print(colors.OKBLUE + '\nTest Valide Semi Avancé\n' + colors.ENDC)
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)

    print('> x^2 = ?')
    print(interpreter.parse('x^2 = ?'), colors.OK if str(interpreter.parse('x^2 = ?')) == '4.0' else colors.KO)
    print('\n')

    print('> f(x) = x + 2')
    print(interpreter.parse('f(x) = x + 2'), colors.OK if str(interpreter.parse('f(x) = x + 2')) == 'x + 2' else colors.KO)
    print('\n')

    print('> p = 4')
    print(exp := str(interpreter.parse('p = 4')), colors.OK if exp == '4.0' else colors.KO)
    print('\n')

    print('> f(p) = ?')
    print(exp := str(interpreter.parse('f(p) = ?')), colors.OK if exp == '6.0' else colors.KO)
    print('\n')

    print('Matrix ** to be tested later')
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)
    print(colors.OKBLUE + '\nTest Valide avancé\n' + colors.ENDC)
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)

    print('> 4-3-(2*3)^2*(2-4)+4 = ?')
    print(exp := str(interpreter.parse('4-3-(2*3)^2*(2-4)+4 = ?')), colors.OK if exp == '77.0' else colors.KO)
    print('\n')

    print('> f(x) = 2*(x+3*(x-4))')
    print(exp := str(interpreter.parse('f(x) = 2*(x+3*(x-4))')), colors.OK if exp == '2 * (x + 3 * (x - 4))' else colors.KO)
    print('\n')

    print('> p = 2')
    print(exp := str(interpreter.parse('p = 2')), colors.OK if exp == '2.0' else colors.KO)
    print('\n')

    print('> f(3) - f(p) + 2 = ?')
    print(exp := str(interpreter.parse('f(3) - f(p) + 2 = ?')), colors.OK if exp == '10.0' else colors.KO)
    print('\n')
    
    print('> f(x) = 2*x*i')
    print(exp := str(interpreter.parse('f(x) = 2*x*i')), colors.OK if exp == '2 * x * i' else colors.KO)
    print('\n')

    print('> f(2) = ?')
    print(exp := str(interpreter.parse('f(2) = ?')), colors.OK if exp == 'i * 4.0' else colors.KO)
    print('\n')

    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)
    print(colors.OKBLUE + 'Test Alambiqués' + colors.ENDC)
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)
    
    print('> f(x) = 2x^2')
    print(exp := str(interpreter.parse('f(x) = 2x^2')), colors.OK if exp == '2 * x^2' else colors.KO)
    print('\n')

    print('> g(z) = (3z%2)^(z/30)')
    print(exp := str(interpreter.parse('g(z) = (3z%2)^(z/30)')), colors.OK if exp == '(3 * z % 2)^(z / 30)' else colors.KO)
    print('\n')

    print('> f(2)^g(1)= ?')
    print(exp := str(interpreter.parse('f(2)^g(1)= ?')), colors.OK if exp == '8.0' else colors.KO)
    print('\n')

    print('> (g(1)-f(1))/((34)^(2.1)) = ?')
    print(exp := str(interpreter.parse('(g(1)-f(1))/((34)^(2.1)) = ? ')), colors.OK if exp == '-0.0006079869733164874' else colors.KO)
    print('\n')

    print('> a = [[3, 2, 3];[2, 4, 1];[4,5, 8]] * 3.4')
    print(exp := str(interpreter.parse('a = [[3, 2, 3];[2, 4, 1];[4,5, 8]] * 3.4')), colors.OK if exp == str(Matrix('', '[[10.2, 6.8, 10.2];[6.8, 13.6, 3.4];[13.6, 17.0, 27.2]]')) else colors.KO)
    print('\n')
    
    print('> a = ?')
    print(exp := str(interpreter.parse('a = ?')), colors.OK if exp == str(Matrix('', '[[10.2, 6.8, 10.2];[6.8, 13.6, 3.4];[13.6, 17.0, 27.2]]')) else colors.KO)
    print('\n')

        
    print('> f(x) =  3x(3 -x )')
    print(exp := str(interpreter.parse('f(x) = 3x(3 -x )')), colors.OK if exp == '3 * x * (3 - 1 * x)' else colors.KO)
    print('\n')
        
    print('> f(-3.4) = ?')
    print(exp := str(interpreter.parse('f(-3.4) = ?')), colors.OK if exp == '-65.28' else colors.KO)
    print('\n')

    
    print('> (3 + 3.5i) / (.7 - 2i) = ?')
    print(exp := str(interpreter.parse('(3 + 3.5i) / (.7 - 2i) = ? ')), colors.OK if exp == '-1.0913140311804008 + i * 1.88195991091314' else colors.KO)
    print('\n')

    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)
    print(colors.OKBLUE + 'Test Negatifs' + colors.ENDC)
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)

    
    print('> -(2)=? ')
    print(exp := str(interpreter.parse('-(2)=? ')), colors.OK if exp == '-2.0' else colors.KO)
    print('\n')

        
    print('> -(-2)=? ')
    print(exp := str(interpreter.parse('-(-2)=? ')), colors.OK if exp == '2.0' else colors.KO)
    print('\n')

    print('> f(x)= 2x+3 ')
    print(exp := str(interpreter.parse('f(x) = 2x+3 ')), colors.OK if exp == '2 * x + 3' else colors.KO)
    print('\n')

    print('> f(-2) = ? ')
    print(exp := str(interpreter.parse('f(-2) = ? ')), colors.OK if exp == '-1.0' else colors.KO)
    print('\n')

    print('> -f(-2)=? ')
    print(exp := str(interpreter.parse('-f(-2) = ? ')), colors.OK if exp == '1.0' else colors.KO)
    print('\n')

    print('> (-f(-2)) =? ')
    print(exp := str(interpreter.parse('(-f(-2)) = ? ')), colors.OK if exp == '1.0' else colors.KO)
    print('\n')

    print('> (-f(-2)^2) =? ')
    print(exp := str(interpreter.parse('(-f(-2)^2) = ? ')), colors.OK if exp == '-1.0' else colors.KO)
    print('\n')

    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)
    print(colors.OKBLUE + 'Test Matrices' + colors.ENDC)
    print(colors.OKBLUE + '\n--------------------------\n' + colors.ENDC)
    
    print('> a = [[2, 1]] ')
    print(exp := str(interpreter.parse('a = [[2, 1]] ')), colors.OK if exp == '[2.0, 1.0]' else colors.KO)
    print('\n')
    
    print('> f(x) = a*x ')
    print(exp := str(interpreter.parse('f(x) = a*x ')), colors.OK if exp == '[[2.0,1.0]] * x' else colors.KO)
    print('\n')
    
    print('> f(2)=? ')
    print(exp := str(interpreter.parse('f(2)=?')), colors.OK if exp == '[4.0, 2.0]' else colors.KO)
    print('\n')

    print('> b = [[2, 1, 2.3, 4.5, 33];[0, 0, 0, 0 ,0];[3, 3, 3, 3, 3]]')
    print(exp := str(interpreter.parse('b =  [[2, 1, 2.3, 4.5, 33];[0, 0, 0, 0 ,0];[3, 3, 3, 3, 3]] ')), colors.OK if exp == '[2.0, 1.0, 2.3, 4.5, 33.0]\n[0.0, 0.0, 0.0, 0.0, 0.0]\n[3.0, 3.0, 3.0, 3.0, 3.0]' else colors.KO)
    print('\n')
    
    print('> f(x) = b*x ')
    print(exp := str(interpreter.parse('f(x) = b*x ')), colors.OK if exp == '[[2.0,1.0,2.3,4.5,33.0];[0.0,0.0,0.0,0.0,0.0];[3.0,3.0,3.0,3.0,3.0]] * x' else colors.KO)
    print('\n')

    print('> f(-23.002)=? ')
    print(exp := str(interpreter.parse('f(-23.002)=?')), colors.OK if exp == '[-46.004, -23.002, -52.904599999999995, -103.509, -759.0659999999999]\n[-0.0, -0.0, -0.0, -0.0, -0.0]\n[-69.006, -69.006, -69.006, -69.006, -69.006]' else colors.KO)
    print('\n')
    
    print('> a = [[1, 2];[-2, 3.3]]')
    print(exp := str(interpreter.parse('a = [[1, 2];[-2, 3.3]]')), colors.OK if exp == '[1.0, 2.0]\n[-2.0, 3.3]' else colors.KO)
    print('\n')

    print('> b = [[-3.4, 1];[2, 0.3]]')
    print(exp := str(interpreter.parse('b = [[-3.4, 1];[2, 0.3]]')), colors.OK if exp == '[-3.4, 1.0]\n[2.0, 0.3]' else colors.KO)
    print('\n')

    print('> a + b + a = ?')
    print(exp := str(interpreter.parse('a + b + a = ?')), colors.OK if exp == '[-1.4, 5.0]\n[-2.0, 6.8999999999999995]' else colors.KO)
    print('\n')
    

    
    cmd =0
    while cmd != 'quit':
        cmd = prompt()
        print(interpreter.parse(cmd))

    if __debug__ :
        print("debug!")

if __name__ == '__main__':
    main()
