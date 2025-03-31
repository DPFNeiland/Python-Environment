


rendaanual = float(input("Digite seu valor de renda anual: R$ "))

if rendaanual > 0 and rendaanual <= 10000.00:
    print(f"Isento de imposto: R$ {rendaanual}")
    
elif rendaanual > 10000.00 and rendaanual <= 25000.00:
    print(f"Imposto de 10,35%: R$ {rendaanual*1.1035:.2f}")
    
elif rendaanual > 25001.00 and rendaanual <= 50000.00:
    print(f"Imposto de 25,42%: R$ {rendaanual*1.2542:.2f}")

elif rendaanual > 50000.00:
    print(f"Imposto de 29,75%: R$ {rendaanual*1.2975:.2f}")

else:
    print("Valor inválido")