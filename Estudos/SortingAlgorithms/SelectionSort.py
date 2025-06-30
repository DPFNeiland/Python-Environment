

# Detailed look at how Selection Sort works

# Big Oh analysis of running time

# Python Selection Sort code

from math import inf

lista = [10,9,8,5,3,7,92,185,78,1,0,65]

tamanho = len(lista)

for i in range(0,tamanho):
    
    min = inf
    indice = -1

    for j in range(i, tamanho):
        
        if(min > lista[j]):
            min = lista[j]
            indice = j
        
    lista[i], lista[indice] = lista[indice], lista[i]
                
print(lista)

# Selection Sort is not a fast sorting algorithm
# because it uses nested loo´s tp sprt

# It is useful only for small data sets

# It runs in O(n²)

# def selection_sort(A):
#     for i in range (0, len(A) - 1):
#         minIndex = i
#         for j in range (i+1, len(A)):
#             if A[j] < A[minIndex]:
#                 minIndex = j
#             if minIndex != i:
#                 A[i], A[minIndex] = A[minIndex], A[i]

#     return A
      
# Lsita = selection_sort(lista)          
# print(Lsita)
