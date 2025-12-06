
n = int(input())
it = 1
while n != 0:
    imoveis = []
    totalPessoas = 0
    totalConsumo = 0
    mediaConsumoLista = []
    mediaConsumoDict = {}
    jaTem = []

    for i in range(n):
        imoveis.append(tuple(map(int, input().split())))

        totalPessoas += imoveis[i][0]
        totalConsumo += imoveis[i][1]

        # 1° é a média de consumo e o 2° é a qtd de pessoas na casa
        mediaConsumoAtual = imoveis[i][1]//imoveis[i][0]

        if mediaConsumoAtual in jaTem:
            mediaConsumoDict[mediaConsumoAtual] += imoveis[i][0]
        else:
            mediaConsumoDict[mediaConsumoAtual] = imoveis[i][0]
            jaTem.append(mediaConsumoAtual)
    
    list(mediaConsumoDict.items()).sort()

    print(f"Cidade# {it}:")
    for pessoas, qtd in mediaConsumoDict.items():
        print(f"{qtd}-{pessoas}",end=" ")
    print()

    print(f"Consumo medio: {int((totalConsumo/totalPessoas * (10 ** 2))) / (10 ** 2):.2f} m3.")
    print()
    it += 1
    n = int(input())