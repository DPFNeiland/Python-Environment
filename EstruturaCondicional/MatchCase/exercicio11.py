




familia = str(input("Digite o nome da família: "))


individuos = int(input("Quantos indivíduos estão incluídos no retrato: "))


match individuos:
    case 1:
        print(f'Família: {familia}')
        print('Preço: R$ 100.00')
        
    case 2:
        print(f'Família: {familia}')
        print('Preço: R$ 130.00')
        
    case 3:
        print(f'Família: {familia}')
        print('Preço: R$ 150.00')    

    case 4:
        print(f'Família: {familia}')
        print('Preço: R$ 165.00')
        
    case 5:
        print(f'Família: {familia}')
        print('Preço: R$ 175.00')
        
    case 6:
        print(f'Família: {familia}')
        print('Preço: R$ 180.00')
    
    case individuos if individuos >= 7:
        print(f'Família: {familia}')
        print('Preço: R$ 185.00')
        
    case _:
        print('Valor inválido')