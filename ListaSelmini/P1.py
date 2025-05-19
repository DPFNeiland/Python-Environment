


# 5 múltiplo seguidos de 3

# numero % 3 = 0

numero = int(input("Digite um número: "))

contador = 0

while contador < 5:
    
    if numero % 3 == 0:
        print(f"{numero}", end=" ")
        contador += 1
    
    numero += 1
    
    
    