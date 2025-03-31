





precoetiqueta = float(input("Digite o preço de etiqueta: "))

codigo = int(input("Digite o código de pagamento: "))

match codigo:
    case 1:
        print(f"À vista em dinheiro ou cheque, recebe 10% de desconto: R$ {precoetiqueta*0.9:.2f}")
        
    case 2:
        print(f"À vista no cartão de crédito, recebe 5% de desconto: R$ {precoetiqueta*0.95:.2f}")
    
    case 3:
        print(f"Em duas vezes, preço normal de etiqueta sem juros, valor de cada parcela: {precoetiqueta/2:.2f}")
    
    case 4:
        print(f"Em três vezes, preço normal de etiqueta mais juros de 10%, valor de cada parcela {precoetiqueta/3*1.10:.2f}")
        
    case _:
        print(f'Código inválido')