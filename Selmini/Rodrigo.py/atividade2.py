

a = int(input('Digite o primeiro valor: '))
b = int(input('Digite o segundo valor: '))
c = int(input('Digite o terceiro valor: '))

maior = a

menor = a

# Saber qual valor é maior
if maior < a:
    maior = a
    
if maior < b:
    maior = b
    
if maior < c:
    maior = c
    
# Saber qual valor é menor

if menor > a:
    menor = a
    
if menor > b:
    menor = b
    
if menor > c:
    menor = c
    
print(f'A diferença entre o maior e o menor valor é: {maior-menor}')