

Si = str(input())
Ki = int(input())

SiList = list(Si)

Lax = True

aux = 0

i = 0


while Lax:
    if((i+Ki) <= len(Si)-1):
        if (Si[i] > Si[i+Ki]):
            SiList[i], SiList[i+Ki] = SiList[i+Ki], SiList[i]
    
    i+=1

    if(Ki < i+2):
        i = 0
        aux += 1
    if(aux == 100):
        Lax = False


Si = ''.join(SiList)

print(Si)
# Si = str(input())
# Ki = int(input())

# tamanho = len(Si)

# SiImpar = []
# SiPar = []
# resp = []
# par = 0
# impar = 0

# for i in range(0,len(Si)):
    
#     if(i%2 == 0):
#         SiPar.append(Si[i])
#     else:
#         SiImpar.append(Si[i])


# for i in range(0, len(Si)):
    
#     if(i%2 == 0):
#         resp.append(SiPar[par])
#         par += 1
#     else:
#         resp.append	(SiImpar[impar])
#         impar += 1

# print(resp)