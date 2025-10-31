from random import randint

MAX = 9
semrepetir = [] 
lista = []

for i in range(MAX):
    aux = randint(0, MAX)

    if not aux in lista:
        semrepetir.append(aux)

    lista.append(aux)
    
print(lista)
print(semrepetir)