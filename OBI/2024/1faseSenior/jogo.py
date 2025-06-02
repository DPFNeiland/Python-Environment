 

def juntaOsZero(Num: int):
    x = ''
    
    for carac in tabAtual[Num]:
        x += carac
    tabAtual[Num] = x
    
def chPrIntAnt(Iterador: int, Num: int, Sinal: int):
    return int(stringAtual[Iterador + Sinal*(N + Num)])

def AnESu(Iterador: int, Num: int):
    return int(stringAtual[Iterador + Num])

def Soma(i: int):
    return chPrIntAnt(i, 3, -1) + chPrIntAnt(i,2,-1) + chPrIntAnt(i, 1, -1) + AnESu(i, -1) + AnESu(i, 1) + chPrIntAnt(i, 1, 1) + chPrIntAnt(i, 2, 1) + chPrIntAnt(i, 3, 1)

N, Q = input().split()

N = int(N)
Q = int(Q)

tabAtual = [['0' for i in range(0,N + 2)] for _ in range(0,N + 2)]
stringAtual = ""
stringProxima = ""

juntaOsZero(0)

juntaOsZero(N + 1)

for i in range(1, N+1):
    x = list(map(str, input().split())) 
    tabAtual[i] = '0' + x[0] + '0'


for i in range(0, N + 2):
    stringAtual += tabAtual[i]


stringProxima = stringAtual

aux = 0

for i in range(N+3, len(stringAtual) - (N + 3)):
    
    if(aux % N == 0):
        i += 2
        print()
    
    print(Soma(i), end="")
    if stringAtual[i] == '0' and (Soma(i) == 3):
        stringProxima = list(stringProxima)
        stringProxima[i] = '1'
        stringProxima = ''.join(stringProxima)

    aux += 1 


print(stringAtual)
print(stringProxima)