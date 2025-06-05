
X = [3, 5, 8, 4, 9, 7, 10, 7, 1, 2]
s, cont = 0, 0

for i in range(0, len(X)):
    s += X[i]


m = s / len(X)

for i in range(0, len(X)):
    if X[i] < m:
        cont += 1

print(cont)