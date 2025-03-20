
list = [0, 2]
listada = [True, True]

def retas(n):

    if(n==1):
        return list[1]
    
    if listada[n]:
        return list(n)
    else:
        listada[n] = True
        list[n] = []
        return retas(n-1) + n

T = int(input())

for i in range(0,T):

    N = int(input())

    
    print(retas(N))
