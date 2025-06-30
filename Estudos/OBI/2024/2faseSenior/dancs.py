N, M, P = map(int, input().split())


matriz = [[i * M + j + 1 for j in range(M)] for i in range(N)]


mapa_linhas = list(range(N))
mapa_colunas = list(range(M))

for _ in range(P):
    op, x, y = input().split()
    x, y = int(x) - 1, int(y) - 1

    if op == 'L':
        mapa_linhas[x], mapa_linhas[y] = mapa_linhas[y], mapa_linhas[x]
    elif op == 'C':
        mapa_colunas[x], mapa_colunas[y] = mapa_colunas[y], mapa_colunas[x]


for i in range(N):
    linha = []
    for j in range(M):
        valor = matriz[mapa_linhas[i]][mapa_colunas[j]]
        linha.append(valor)
    print(*linha)
