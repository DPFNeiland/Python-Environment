

N = 1

MAX_N = 100000

fatoriais = [1] * (MAX_N + 1)

for i in range(2, MAX_N + 1):
    fatoriais[i] = (fatoriais[i - 1] * i)


while N != 0:
    N = int(input())
    
    if N == 0:
        break
    
    if N == 3 :
        print("1")
    else:
        print(f"{fatoriais[N]%1000000009:.0f}")