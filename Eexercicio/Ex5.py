



a = int(input('Digite o valor de A: '))
b = int(input('Digite o valor de B: '))
c = int(input('Digite o valor de C: '))


if (b > a) and (b > c):
    aux = b
    b = a
    a = aux
elif (c > a) and (c > b):
    aux = c
    c = a
    a = aux
    
if (a**2 == (b**2 + c**2)):
    print('retângulo')
elif (a**2 < (b**2 + c**2)):
    print('acutângulo')
elif (a**2 > (b**2 + c**2)):
    print('obtusângulo')