
inicio = 0
fim = 0

numerosRaros = 0
numerosRarosPar = 0
numerosRarosImpar = 0

while not (inicio > 999 and inicio < 10000) and not (fim >= 1000 and fim <= 9999):
    print("Digite valores de 4 dígitos! (caso contrário, será necesssário inserir novamente)")
    inicio = int(input("Digite o início do intervalor: "))
    fim = int(input("Digite o fim do intervalo: "))

'''
    Se o início do intervalor for maior que o fim,
    ele troca os valores para continuar normalmente
    a lógica do código
    
'''

for i in range(inicio, fim+1):
    numero = str(i)
    
    if int(numero[0]) + int(numero[1]) == int(numero[2]) + int(numero[3]):
        numerosRaros += 1
        
        print(numero)

        if i % 2 == 0:
            numerosRarosPar += 1
            
        else:
            numerosRarosImpar += 1
            
print(f"Quantidade de raros no intervalo acima: {numerosRaros}")
print(f"Quantidade de raros pares no intervalo acima: {numerosRarosPar}")
print(f"Quantidade de raros ímpares no intervalo acima: {numerosRarosImpar}")
