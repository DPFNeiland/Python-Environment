


primeiro = 0
segundo = 1

N = int(input("Digite um valor: "))

for i in range(0,N-2):
    primeiro, segundo = segundo, segundo + primeiro
    
if N == 1:
    print(f'N: 0')
    
elif N == 2:
    print(f'N: {segundo}')
    
else:
    print(f'N: {segundo}')