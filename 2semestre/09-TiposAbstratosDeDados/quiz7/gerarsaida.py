
def gerar(M, n):
    for L in range(1, n + 1):
        for C in range(1, L + 1):
            if C == 1 or L == C:
                M[L][C] = 1
            else:
                M[L][C] = M[L - 1][C] + M[L - 1][C - 1]

def saida(M, n):
    for L in range(1, n + 1):
        for C in range(1, L + 1):
            print(f"{M[L][C]:3d}", end="")
        print()
n = 5
M = [[0] * (n + 1) for _ in range(n + 1)]

gerar(M, n)
saida(M, n)