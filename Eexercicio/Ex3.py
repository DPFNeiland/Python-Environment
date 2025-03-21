
from math import ceil

PI = 3.141592653589793238462643383279502884197169399375105820974944592307816406

# 3 m² por unidade comprada

Altura = float(input('Digite a altura do reservatório (em metros): '))

Raio = float(input('Digite o raio do reservatório: '))

CustoUni = float(input('Digite o custo de cada unidade de isolamento: '))

Area = 2*PI*(Raio**2 + Raio*Altura)

print(f'Área toal a ser isolada: {Area:.2f}')

Qui = ceil(Area*1.05 / 3) # ceil(Area/3) 

print(f'Quantidade de unidade de isolamento: {Qui}')

CustoTotal = Qui * CustoUni

print(f'Custo total: R$ {CustoTotal:.2f}')