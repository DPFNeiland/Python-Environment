


binary = int(input("Digite um valor em binário de 4 bits: "))

UnidadeDeDezena = binary - binary%1000
Centena = binary%1000 - binary%1000%100
Dezena = binary%1000%100 - binary%1000%100%10
Unidade = binary%1000%100%10

print(f" O valor decimal do valor binário é : {
    Unidade * pow(2,0) + 
    Dezena/10 * pow(2,1) +
    Centena/100 * pow(2,2) + 
    UnidadeDeDezena/1000 * pow(2,3) }") 



'''
binary = int(input("Digite um valor em binário de 4 bits: "))

UnidadeDeDezena = binary - binary%1000
Centena = (binary - UnidadeDeDezena) - (binary - UnidadeDeDezena)%100
Dezena = (binary - UnidadeDeDezena - Centena) - (binary - UnidadeDeDezena - Centena) %10
Unidade = (binary - UnidadeDeDezena - Centena - Dezena)

print(f" O valor decimal do valor binário é : {Unidade * pow(2,0) + Dezena/10 * pow(2,1) + Centena/100 * pow(2,2) + UnidadeDeDezena/1000 * pow(2,3)}") 
'''