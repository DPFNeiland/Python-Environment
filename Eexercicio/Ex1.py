




Numero = int(input('Digite o número: '))

Centena = Numero//100
Numero = Numero - Centena*100

Dezena = Numero//10
Numero = Numero - Dezena*10

NumeroVerificador = (Centena + Numero)*100 + (Dezena + Dezena)*10 + Numero+Centena

print(f'{NumeroVerificador}')

if (NumeroVerificador>=1000):
    UnidadeDeDezena = NumeroVerificador//1000
    NumeroVerificador = NumeroVerificador - UnidadeDeDezena*1000
    
    Centena = NumeroVerificador//100
    NumeroVerificador = NumeroVerificador - Centena*100
    
    Dezena = NumeroVerificador//10
    NumeroVerificador = NumeroVerificador- Dezena*10
    
    DigitoVerificador = UnidadeDeDezena*1 + Centena*2 + Dezena*3 + NumeroVerificador*4
    
    DigitoVerificador = DigitoVerificador - DigitoVerificador//100*100 - DigitoVerificador//10*10 
    
    print(DigitoVerificador)
    
elif (NumeroVerificador >= 100 and NumeroVerificador<=999):
    Centena = NumeroVerificador//100
    NumeroVerificador = NumeroVerificador - Centena*100
    
    Dezena = NumeroVerificador//10
    NumeroVerificador = NumeroVerificador- Dezena*10
    
    DigitoVerificador = Centena*1 + Dezena*2 + NumeroVerificador*3    
    
    DigitoVerificador = DigitoVerificador - DigitoVerificador//100*100 - DigitoVerificador//10*10 
    
else:
    print('Digite um valor válido (3 dígitos): ')

print(DigitoVerificador)
    