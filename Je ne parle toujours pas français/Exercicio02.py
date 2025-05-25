
n = -1
maior = 0


while n < 1:
    n = int(input('Informe algum número: '))

if n == 1:
    print('O seu número não possui um fator primo :(')

else: 
    for i in range (1, n + 1):
        
        if n % i == 0:
            ehprimo = True
            
            for j in range(2, int(i ** (1/2) + 1)):
                
                if i % j == 0:
                    ehprimo = False
                    
            if (ehprimo or i == 2 or i == 3) and maior < i:
                maior = i
    
    print(f'O maior fator primo divisor de {n} é: {maior}')
   
