





P = int(input())

C = []
C.append(int(input()))
C.append(int(input()))
C.append(int(input()))
C.sort()

sum = 0
cont = 0

for i in range(0,3):
    sum += C[i]
    if P >= sum:
        cont += 1

    
print(f"{cont}")