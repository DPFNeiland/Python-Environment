

A = [5, 2, 4, 6, 1, 3]

for j in range(len(A) - 1):
    minimo = A[j]
    index = j
    
    for i in range(j, len(A)):
        if A[i] < minimo:
            index = i
            minimo = A[i]
    
    aux = A[j] 
    A[j] = A[index]
    A[index] = aux
    
print(A)