
from math import ceil

PI = 3.141592653589793238462643383279502884197169399375105820974944592307816406

# 3 m² por unidade comprada

Altura = float(input('Digite a altura do reservatório (em metros e maior que 0): '))

if(Altura <= 0):
    print('Digite um valor válido para a altura.')
    
else:    
    Raio = float(input('Digite o raio do reservatório (em metros e maior que 0): '))

    if(Raio <= 0):
        print('Digite um valor válido para o raio.')
    
    else:        
        CustoUni = float(input('Digite o custo de cada unidade de isolamento (em R$ e maior que 0): '))

        if(CustoUni <= 0):
            print('Digite um valor válido para o custo unitário.')
    
        else:
            Area = 2*PI*(Raio**2 + Raio*Altura)

            print(f'Área toal a ser isolada: {Area:.2f}')

            Qui = ceil(Area*1.05 / 3) 
            
            print(f'Quantidade de unidade de isolamento: {Qui}')

            CustoTotal = Qui * CustoUni

            print(f'Custo total: R$ {CustoTotal:.2f}')