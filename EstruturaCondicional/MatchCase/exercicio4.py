



idade = int(input("Digite a idade: "))

print(f'{idade} {idade >= 5} and {idade <= 7}')

match idade:
    case idade if idade >= 5 and idade <= 7:
        print("Infantil A")
    
    case idade if idade >= 8 and idade <= 10: 
        print("Infantil B")
    
    case idade if idade >= 11 and idade <= 13:
        print("Juvenil A")
    
    case idade if idade >= 14 and idade <= 17:
        print("Juvenil B")
    
    case idade if idade >= 18:
        print("Adulto")
    
    case _:
        print('inválido ')