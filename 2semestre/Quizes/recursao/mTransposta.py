

m = [[1, 2], [2, 3], [3, 4]]
t = [[0, 0, 0], [0, 0, 0]]

for i in range(0, len(m)):
    for j in range(0, len(m[i])):
        t[j][i] = m[i][j]
        
print(t)