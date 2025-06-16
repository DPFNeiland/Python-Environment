
N = int(input())

X = list(map(int,input().split()))

H = X[0]
for i in range(0, len(X)):
    if H < X[i]:
        H = X[i]

grafico_transposto = [[0 for _ in range(H)] for _ in range(N)]


for i in range(len(grafico_transposto)):
    for j in range(X[i]):

        grafico_transposto[i][j] = 1

grafico = []
for i in range(H):
    grafico.append([row[i] for row in grafico_transposto])



for i in range(H - 1, -1, -1):
    for j in range(N):
        print(grafico[i][j], end=" ")
    print()