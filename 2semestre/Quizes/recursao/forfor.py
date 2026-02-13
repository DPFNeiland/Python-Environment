

a = [[3, 2], [-4, 6]]
b = [[0 for _ in range(2)] for _ in range(2)]

for i in range(0, len(a)):
    for j in range(0, len(b)):
        b[j][i] = a[i][j]
        
print(b)