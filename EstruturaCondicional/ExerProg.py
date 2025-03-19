


resultado = 0

dias = int(input("Digite os dias que ficou diariamente: "))

if(dias<15):
    resultado += dias*(88+300)
elif(dias==15):
    resultado += dias*(56+300)
else:
    resultado += dias*(22.5+300)
    
print(f"O preço a ser pago é R${resultado}")