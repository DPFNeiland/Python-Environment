

N = int(input())

resp = 1

for i in range(0,N):

    aux = int(input())
    
    if(i == 0):
        anterior = aux
    
    if(aux != anterior):
        anterior = aux  
        resp +=1
        
print(resp)