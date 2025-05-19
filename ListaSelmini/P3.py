



inicio = int(input("Digite o início do intervalo: ")) 

fim = int(input("Digite o fim do intervalo: ")) 

soma = 0

if inicio > fim:
    inicio, fim = fim, inicio
    
for i in range(inicio, fim + 1):
    
    if (i % 2 == 1 ):
        print(i)
        soma += i
        
print(f'A soma dos valores ímpares é: {soma}')