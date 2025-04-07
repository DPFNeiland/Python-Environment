
lista = [1,2,3]



while not (lista[0] == 0) and not (lista[1] == 0) and not (lista[2] == 0):
    
    A, B, C = input().split()
    
    lista[0] = int(A)
    lista[1] = int(B)
    lista[2] = int(C)
    
    if not (lista[0] == 0) and not (lista[1] == 0) and not (lista[2] == 0):
        continue
    
    lista.sort()
    
    if(lista[0] + lista[1] > lista[2]) and (lista[1] + lista[2] > lista[0]) and (lista[2] + lista[0] > lista[1]):
        
        if (lista[0] == lista[1]) and (lista[0] == lista[2]) and (lista[1] == lista[2]):
            print('Equilátero')
        
        elif (lista[0] == lista[1]) or (lista[0] == lista[2]) or (lista[1] == lista[2]):
            print('Isósceles')
        
        else:
            print('Escaleno')
        
    else:
        print('não é um triângulo')