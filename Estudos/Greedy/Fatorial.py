


def fatorial(N: int) -> int:
    if N == 1:
        return 1
    
    return N*fatorial(N-1)



N = int(input())

fatActual = 1
resp = 0

while  N > fatorial(fatActual):
    fatActual += 1

fatActual -=1

while True:
    if N >= fatorial(fatActual):
        N -= fatorial(fatActual)
        resp += 1

    if N < fatorial(fatActual):
        fatActual -= 1
    
    

    if N == 0:
        break

print(resp)