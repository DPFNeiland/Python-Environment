


x = []
f = 0
l = 0
num = 0

for i in range(4):
    aux = str(input())
    
    x.append(aux)
t = len(x[0]) - 1

for i in range(4):
    f += int(x[i][0])*(10**(3-i))
    l += int(x[i][t])*(10**(3-i))

for i in range(1, t):
    num = 0
    
    for j in range(4):
        num += int(x[j][i])*(10**(3-j))
        
    print(chr((f*num+l)%257), end="")
print()