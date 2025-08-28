

lista = [1, 2, 3]

A, B, C = input().split()

lista[0] = int(A)
lista[1] = int(B)
lista[2] = int(C)

lista.sort()

if lista[0] == lista[1] or lista[0] == lista [2] or lista[1] == lista[2]:
    print('S')

elif lista[0] + lista[1] == lista[2]:
    print('S')

else:
    print('N')