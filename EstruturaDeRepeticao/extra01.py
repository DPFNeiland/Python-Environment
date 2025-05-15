


'''
    o seu programa deverá ler pelo terminal um valor na base binária.
    o seu programa deverá converter o valor lido para a base decimal.
        
'''

aux = 1

while aux != "-1":

    aux = str(input("Digite o valor em base binária: "))
    
    if aux == "-1":
        break

    tamanho = len(aux)

    total = 0

    for caractere in range (tamanho):
        
        if aux[caractere] == '1':
            total += (2**(tamanho - caractere - 1))
            
    print(f'Valor convertido: {total}')