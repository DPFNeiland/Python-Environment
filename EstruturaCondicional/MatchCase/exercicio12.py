



morango = float(input("Digite o número de quilos de morango comprados: Kg "))

maca = float(input("Digite o número de quilos de maça comprados: Kg "))

banana = float(input("Digite o número de quilos de banana comprados: Kg "))

total = float(0.0)

if morango >= 0 and morango <= 5:
    total += morango * 2.5
    
else:
    total += morango * 2.2
    
    

if maca >= 0 and maca <= 5:
    total +=  maca * 1.8
    
else:
    total += maca * 1.5



if banana >= 0 and banana <= 5:
    total += banana * 1.0
    
else: 
    total += banana * 0.87
    

if total > 25.00:
    print(f"Desconto de 10% do total da compra: R$ {total*0.9:.2f}")
    
else:
    print(f"Total da compra: R$ {total:.2f}")