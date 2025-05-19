
listaDeNumeros = []

soma = 0

n = int(input("Digite um valor: "))

for i in range(0, n):
    
    listaDeNumeros.append(int(input(f"Digite o {i+1}º valor: ")))
    soma += listaDeNumeros[i]
    
print(f'A soma dos valores digitados é: {soma}')
print(f'A média aritmética dos valores digitados é: {soma/n:.2f}')