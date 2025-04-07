


valordoproduto = float(input("Digite o valor do produto: R$ "))

if valordoproduto > 0 and valordoproduto < 20.00 :
    print(f"Valor a ser revendido: R$ {valordoproduto*1.45:.2f}")

elif valordoproduto >= 20.00 and valordoproduto < 100.00:
    print(f"Valor a ser revendido: R$ {valordoproduto*1.30:.2f}")
    
elif valordoproduto >= 100.00:
    print(f"Valor a ser revendido: R$ {valordoproduto*1.20:.2f}")
    
else:
    print("Valor inválido.")