from sympy import symbols, sympify
from cmath import sqrt


x = symbols('x')

equacao = input("Digite a equação (Ex.: ax^2 + bx + c): ")

expressao = sympify(equacao)


a = expressao.coeff(x, 2)  

if(a == 0):
    print("A == 0 resulta uma equação de primeiro grau")

b = expressao.coeff(x, 1)  
c = expressao.coeff(x, 0)  
if b**2 < 4*a*c:
    '''
    real1, imag1 = x1.real, x1.imag
    real2, imag2 = x2.real, x2.imag 
    
    print(f"Raiz 1: {real1:.2f} + {imag1:.2f}i")
    print(f"Raiz 2: {real2:.2f} - {imag2:.2f}i")
    '''
    print("Delta menor que 0")
else:
 

    x1 = (-b + sqrt(b**2-4*a*c))/(2*a)
    x2 = (-b - sqrt(b**2-4*a*c))/(2*a)
    
    print(f"Raiz 1: {x1:.2f}")
    print(f"Raiz 2: {x2:.2f}")
