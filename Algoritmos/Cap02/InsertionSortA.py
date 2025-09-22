

# A = [123, 321, 343, 432, 412, 321, 324, -423, -42, -423]
A = [5, 2, 4, 6, 1, 3]
chave = 0

for j in range(1, len(A)):
    chave = A[j] 
    
    # Inserir A[j] na sequência ordenada A[1.. j - 1].
    i = j - 1
    while i >= 0 and A[i] > chave:
        A[i + 1] = A[i]
        i = i - 1
    A[i + 1] = chave
    
print(A)
    