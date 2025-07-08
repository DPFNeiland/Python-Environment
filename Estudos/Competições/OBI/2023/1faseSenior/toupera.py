

S, T = input().split()

# salas = [ _ for _ in range(int(T))]

salas = [[] for _ in range(int(S) + 1)]

for i in range(int(T)):
    sala1, sala2 = input().split()
    sala1 = int(sala1)
    sala2 = int(sala2) 
    
    salas[sala1].append(sala2)
    salas[sala2].append(sala1)
    
# print(salas)
    
P = int(input())

passeisoPossiveis = 0

for i in range(P):
    passeio = list(map(int, input().split()))
    
    passeio.reverse()
    passeio.pop()
    passeio.reverse()
    
    # print(passeio)
    
    for i in range(0, len(passeio) - 1):
        # print(f"{passeio[i + 1]} in {salas[passeio[i]]}")
        # print(f"{passeio[i + 1] in salas[passeio[i]]}")
        if not (passeio[i + 1] in salas[passeio[i]]):
            break
        
        # print(i)
    if len(passeio) -2 == i:
        passeisoPossiveis += 1
            
print(passeisoPossiveis)