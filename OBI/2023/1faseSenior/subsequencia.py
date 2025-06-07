


A, B = input().split()

A = int(A)
B = int(B)


sequencia = list(map(int, input().split()))
subsequencia = list(map(int, input().split()))

aux = 0
for num in sequencia:
    if aux == len(subsequencia):
        break
    
    
    if subsequencia[aux] == num:
        aux += 1
        
print(f"{"S" if aux == len(subsequencia) else "N"}")