

v = [5,8,7,5,11,2,10,14,8,5]

x,y, aux= 0,0,0

while x < len(v):
    if v[x] > y:
        y = v[x]
        aux +=1
        
    x+= 1
    
aux = aux * y

print(aux)