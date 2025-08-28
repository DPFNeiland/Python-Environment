

def retas(n):
    
    if(n%2 == 0):
        return (n)*(n+1)/2 +1
    else:
        return (n)*(n+1)/2+1

T = int(input())



for i in range(0,T):

    N = int(input())

    
    print(f'{retas(N):.0f}')


# list = [0, 2]
# listada = [True, True]

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