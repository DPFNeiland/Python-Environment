



a = int(input('Digite o valor de A do triângulo (maior que 0): '))

if (a <= 0):
    print('Digite um valor válido para A.')
    
else:
    b = int(input('Digite o valor de B do triângulo (maior que 0): '))    
    
    if(b <= 0):
        print('Digite um valor válido para B.')
        
    else:      
        c = int(input('Digite o valor de C do triângulo (maior que 0): '))

        if(c <= 0):
            print('Digite um valor vpalido para C')
            
        else:
            
            if (b > a) and (b > c):
                aux = b
                b = a
                a = aux
                
            elif (c > a) and (c > b):
                aux = c
                c = a
                a = aux
            
            if (a > b+c) or (b > a+c) or (c > a+b):
                print('Triângulo inexistente')
                
            elif (a**2 == (b**2 + c**2)):
                print('retângulo')
                
            elif (a**2 < (b**2 + c**2)):
                print('acutângulo')
                
            elif (a**2 > (b**2 + c**2)):
                print('obtusângulo')