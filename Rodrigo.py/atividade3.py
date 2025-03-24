

bicletas = int(input('Número de bicicletas total disponíveis para alugar na empresa: '))

alugueldiario = float(input('Digite o valor do aluguel diário de cada bicicleta em reais (R$): '))

FaturamentoAnual = (bicletas)*(alugueldiario*120)

Multa = (bicletas/10)*(alugueldiario)

print(f'O faturamento anual com o serviço de bicicletas é de: R$ {FaturamentoAnual:.2f}')

print(f'O ganho mensal com multas é de: R$ {Multa:.2f}')
