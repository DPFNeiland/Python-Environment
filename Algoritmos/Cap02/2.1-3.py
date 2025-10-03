

# A = [123, 321, 343, 432, 412, 321, 324, -423, -42, -423]
A = [5, 2, 4, 6, 1, 3]
v = int(input())
chave = 0

print(A)
i = 0
while v != A[i]:
    i = i + 1  
    
    if i == len(A):
        i = -1
        break

print(i)