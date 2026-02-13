def conta_digitos(n):

    if n < 0:
        return [0] * 10
    contagem = [0] * 10
    fator = 1
    
    while fator <= n:
        menor = n % fator
        atual = (n // fator) % 10
        maior = n // (fator * 10)

        for d in range(10):
            contagem[d] += maior * fator

        for d in range(atual):
            contagem[d] += fator
        contagem[atual] += menor + 1

        contagem[0] -= fator

        fator *= 10
    return contagem


while True:
    A, B = map(int, input().split())
    if A == 0 and B == 0:
        break

    resultado = [conta_digitos(B)[i] - conta_digitos(A - 1)[i] for i in range(10)]
    print(" ".join(map(str, resultado)))
