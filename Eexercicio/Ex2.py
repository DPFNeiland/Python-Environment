


Aplicar = float(input('Digite o valor constante da aplicação (Em R$ e maior que 0): '))

if(Aplicar <= 0):
    print('Digite um valor válido para o valor constante da aplicação.')
else:
    TaxaJuros = float(input('Digite o valor da taxa (entre 0 e 1): '))

    if (TaxaJuros > 0) and (TaxaJuros < 1):
        Meses = int(input('Digite o número de meses que a aplicação ficará (maior que 0): '))
        
        if(Meses <= 0):
            print('Digite um valor válido para meses.')
        
        else:
            valor_acumulado = Aplicar*((1+TaxaJuros)**Meses -1)/(TaxaJuros)
        
            print(f'O valor acumulado ao final de {Meses} mês/meses é de: R$ {valor_acumulado:.2f}')
        
    else:
        print('Digite um valor válido para a Taxa.')