# Fatorial (soma dos números)

numero = -1

fatorial = 1

soma = 0

while not numero >= 0:
    numero = int(input("Digite um número inteiro positivo: "))

    
for i in range(1, numero + 1):
    fatorial *= i
    
    
for num in str(fatorial):
    soma += int(num) 
    
print(f'A soma dos dígitos do fatorial de {numero} é {soma}')