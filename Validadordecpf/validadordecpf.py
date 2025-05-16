
# Problema motivador: ***.569.542-**
# É um cpf válido

# a b c 5 6 9 5 4  2  p1 p2

# a * 1 + b * 2 + c * 3 + 





















# Ex: 010.593.932 - 39

# CPF: 0 1 0 5 9 3 9 3  2  3 9 

# 0 1 0 5 9 3 9 3: Dígitos únicos

# 2: Origem

# 3 9: Dígitos verificadores

lista = [0, 1, 0, 5, 9, 3, 9, 3, 2]

# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]

sum = 0
for i in range(1, len(lista)+1):
    sum += (i*lista[i-1])
    
primeirodigito = sum%11

if primeirodigito == 10 :
    primeirodigito = 0
    

lista.append(primeirodigito)

sum = 0
for i in range(0, len(lista)):
    sum += (i*lista[i])
    
segundodigito = sum%11

if segundodigito == 10 :
    segundodigito = 0
    
lista.append(segundodigito)

for i in lista:
    print(i,end='')