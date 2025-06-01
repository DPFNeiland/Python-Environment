



Qtd, Nc = input().split()

Qtd = int(Qtd)

notas = list(map(int, input().split()))

notas.sort()
notas.reverse()


print(notas[int(Nc) - 1])
