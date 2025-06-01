

N = int(input())

t = 0
cont = int(0)
receb = [[] for _ in range(100)]
tempos = [0] * 100
resp = [False] * 100
valores = set()       

for i in range(N):
    Ch, Nm = input().split()
    Nm = int(Nm)
    
    if Ch == 'T':
        t += Nm
        cont = int(0)
        
    if Ch == 'R':
        if cont >= 1:
            t += 1

        receb[Nm] = t
        resp[Nm] = False
        valores.add(Nm)
        

        
        cont += 1
        
        
    if Ch == 'E':
        if cont >= 1:
            t += 1

        tempos[Nm] += t - receb[Nm] 
        resp[Nm] = True

        cont += 1


for i in valores:
    if not resp[i]:
        tempos[i] = -1



for i in range(len(tempos)):
    if tempos[i] != 0:
        print(f'{i} {tempos[i]}')