

N = int(input())

total = ""

for i in range(0, N + 1):
    numeros = list(map(str, input().split()))
    
    
    for numbers in numeros:
        total += numbers    
    


for i in range(0, N):
    const = (N + 1) * i

    for j in range(0, N):
        if int(total[j + const]) + int(total[j + 1 + const]) + int(total[j + N + 1 + const]) + int(total[j + N + 2+ const]) >= 2:
            print('S', end="")
        else:
            print('U', end="")
            
    print()