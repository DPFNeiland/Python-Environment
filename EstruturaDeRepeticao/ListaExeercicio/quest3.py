
numeros = []

for j in range(0, 1000):
    
    numero = int(input("Digite um valor: "))
    
    numeros.append(numero)


for j in range(0, 1000):
    ehprimo = True

    partinteira = int(numeros[j]//(numeros[j]**(1/2)))

    if numeros[j] == 1 :
        ehprimo = False

    else:
        for i in range(2, partinteira + 1):
            if(numeros[j] % i == 0):
                ehprimo = False
                break    
        
    print(f'{numeros[j] if ehprimo else ""}', end=" ")
