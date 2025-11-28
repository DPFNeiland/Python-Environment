from ponto import Ponto

# lista de pontos
lista = list() # construtor
##

for i in range(3):
    print(f"Ponto {i+1}")
    x = float(input())
    y = float(input())
    lista.append(Ponto(x, y))
    print('-' * 20)

print(f'Distância de todos os pontos da origem')
for pontos in lista:
    distancia = pontos.calcular_distancia()
    print(f'{f'{pontos.imprimir_Ponto()}':>9} -> {distancia:.2f}')