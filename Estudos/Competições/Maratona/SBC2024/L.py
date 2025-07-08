

cnt = [0 for _ in range(30)] 
N = int(input())
a = list(map(int, input().split()))



# Conta quantos bits tem cada número
for number in a:
    
    j = 0
    
    # Roda todos os bits do número pra contar
    while (1 << j) <= number:
        
        cnt[j] += 1 if ((1 << j) & number) else 0 
         
        j += 1


print(cnt)
for i in range(N):
    
    prox = 0
    for j in range(30):
        if cnt[j] > 0:
            prox |= (1 << j)
            cnt[j] -= 1
            
    print(f"{prox} {'\n' if i == N - 1 else ''}", end="")
print()