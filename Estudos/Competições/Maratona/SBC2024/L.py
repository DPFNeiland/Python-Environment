

cnt = [0 for _ in range(30)] 
N = int(input())
a = list(map(int, input().split()))



# Conta quantos bits tem cada número
for number in a:
    
    j = 0
    
    # Roda todos os bits do número pra contar
    while (1 << j) <= number:
                    # Conta o 1 deslocado j vezes e faz um AND com number, se o resultado for
                    # diferente de 0, ele incrementam em 1, senão, ele faz nada 
        cnt[j] += 1 if ((1 << j) & number) else 0 
         
        j += 1


print(cnt)
for i in range(N):
    
    prox = 0
    # roda todo o vetor cnt
    for j in range(30):
        # Enquanto existir bit em j, ele executa
        if cnt[j] > 0:
            # faz um OR entre o prox e o bit 1 deslocado j vezes
            prox |= (1 << j)
            
            # Decrementa esse valor no bit
            cnt[j] -= 1
            
    print(f"{prox} {'\n' if i == N - 1 else ''}", end="")
print()