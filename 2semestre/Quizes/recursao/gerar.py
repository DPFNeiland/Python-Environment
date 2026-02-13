

def gerar(m):
    for i in range(0, len(m)):
        for j in range(0, len(m[i])):
            if i < j:
                m[i][j] = 2 * i + 7 * j - 2
            elif i == j:
                m[i][j] = 3 * i * i - 1
            elif i > j:
                m[i][j] = 4 * i * i * i - 5 * j * j

m = [[0 for _ in range(3)] for _ in range(3)]

gerar(m)

print(m)