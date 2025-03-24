

peso = float(input('Digite o peso em quilogramas: (kg) '))

if (peso <= 0):
    print('Digite um valor válido para o peso.')

else:
    altura = float(input('Digite a altura em metros: '))
    
    if(altura <= 0):
        print('Digite um valor válido para a altura.')
        
    else:
        IMC = peso/(altura**2)
        print(f'Índice de massa corporal (IMC): {IMC:.2f}')
        
        if(IMC <= 24.9):
            print('Paciente tem peso normal')
        else:
            print('Paciente tem sobrepreso')