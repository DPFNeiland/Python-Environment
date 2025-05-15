


lista = [10,9,8,5,3,7,92,185,78,1,0,65]


n = len(lista)


for i in range(0,n - 1):
    for j in range(0, n-1-i):
        if lista[j] > lista[j+1]:
            lista[j], lista[j+1] = lista[j+1], lista[j]
        
        print(lista)
print(lista)
        