while True:
    N = int(input())
    if N == 0:
        break

    max_value = 2 ** (2 * (N - 1))
    width = len(str(max_value))

    for i in range(N):
        linha = []
        for j in range(N):
            valor = 2 ** (i + j)
            linha.append(f"{valor:>{width}}")
        print(" ".join(linha))
    print()  
