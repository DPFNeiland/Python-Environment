
bacterias = "A"

segundos, qtdregras = input().split()
segundos = int(segundos)
qtdregras = int(qtdregras)

regras = {}

novasBacterias = ""


for i in range(0,qtdregras):
    antes, atual = input().split()
    
    regras[antes] = atual
    


for j in range(0, segundos ):
    
    novasBacterias = ""
    actual = bacterias[0]



    for i in range(0, len(bacterias) - 1):
        
        
        if bacterias[i] == bacterias[i + 1]:
            actual += bacterias[i + 1]
        
        else:
            novasBacterias += regras[actual]             
            actual = str(bacterias[i + 1])
            
    novasBacterias += regras[actual]
        
    while len(bacterias) == 1 and j < segundos:
        novasBacterias = regras[actual]
        j += 1
        
    if j + 1 == segundos:
        break
    
    bacterias = novasBacterias
    
a = 0
b = 0

for i in range(0, len(novasBacterias)):            
    
    if novasBacterias[i] == "A":
        a +=1
    else: 
        b +=1
        
print(f'{a} {b}')  
    
    