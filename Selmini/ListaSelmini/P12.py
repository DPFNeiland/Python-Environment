
maior = 1
inicio = 100
fim = 1000

for i in range(inicio,fim):
    
    for j in range(inicio, fim):    
        mult = str(i * j)        
        
        ehPalindromo = True
        
        tam = len(mult)

        for k in range(0,int(tam/2)):


            if(mult[k] != mult[tam-k-1]):
                ehPalindromo = False
        
        if ehPalindromo:
            if(maior < int(mult)):
                maior = int(mult)           
            
print(maior)
            