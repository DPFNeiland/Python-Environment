


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





# def retas(n):

#     # if(n==1):
#     #     return 2
    
#     # if(listada[i]):
#     #     return lista[i]
#     # else:
#     #     listada[i] = True
#     #     lista[i] = retas(n-1) + n
#     #     return lista[i]

#     resp = 2

#     for i in range (1,n):
#         resp+-n
    
#     return resp
        

# T = int(input())

# lista = [0,2]
# listada = [False]

for i in range(0,T):

    N = int(input())

    
    print(retas(N))
