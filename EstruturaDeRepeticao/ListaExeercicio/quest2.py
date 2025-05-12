
lista = []

par = 0
impar = 0


for i in range(0, 1000):
    
    aux = int(input("Digite o valor: "))
    
    lista.append(aux)
    
    if (aux % 2 == 0):
        par += 1
        
    else:
        impar += 1
        
        
print(f'Quantidade de números ímpares: {impar}')
print(f'Quantidade de números pares: {par}')

print(f'Quantidade de números ímpares relativo: {impar/5}')
print(f'Quantidade de números par relativo: {par/5}')
