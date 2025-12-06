from ponto import Ponto
lista = []
quantidade = int(input("Qual a quantidade de pontos?"))
for _ in range(quantidade):
    x = int(input("Coordenada x -->"))
    y = int(input("Coordenada y -->"))
    lista.append(Ponto(x, y))

print('Distância de cada ponto até a origem')
for ponto in lista:
    print(f"{ponto}  ->  {ponto.calcular_distancia_da_origem()}")

print(lista[0].calcular_distancia(lista[1]))















# from ponto import Ponto
# from random import randint

# # lista de pontos
# lista = list() # construtor
# N = 4

# for i in range(N):
#     # x = float(input())
#     # y = float(input())
#     x = randint(-N**2, N**2-1)
#     y = randint(-N**2, N**2-1)
#     print(f"Ponto {i+1} -> {x} e {y}")
#     lista.append(Ponto(x, y))
#     print('-' * 20)

# print(f'Distância de todos os pontos da origem')
# for pontos in lista:
#     distancia = pontos.calcular_distancia_da_origem(0)
#     print(f'{f'{pontos.imprimir_Ponto()}':>9} -> {distancia:.2f}')