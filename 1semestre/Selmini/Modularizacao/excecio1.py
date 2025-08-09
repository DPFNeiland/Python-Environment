
def verificadorDigito(num):
    for nume in range(1, num//2 + 1):
        if num % nume == 0:
            print(nume, end=" ") 

N = int(input("Digite quantos valores positivos: "))
j = 0
positivos = []

while j < N: 
    x = int(input("Digite o valor: "))
    
    if x < 0:
        print("Digite um valor válido!!!")
        
    else:
        positivos.append(x)
        j += 1
        
for numeros in positivos:
    verificadorDigito(numeros)
    
    print()