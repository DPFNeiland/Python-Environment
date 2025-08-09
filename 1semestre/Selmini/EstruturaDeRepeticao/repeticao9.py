
pagar = int(1)

subtotal = float(0.0)

while pagar != 2:
    
    Qtd = int(input('Digite a quantidade do produto: '))
    Valor = float(input('Digite o valor do produto: R$ '))
    
    subtotal += Qtd * Valor
    
    pagar = int(input('Você deseja realizar o pagamento? Digite 2, senão, digite qualquer valor: '))
    
print(f'Sutotal: R$ {subtotal}')
print('À vista com 10% de desconte: código 1')
print('Em duas vezes com um acréscimo de 15.5%: código 2')
pagar = int(input('Digite sua forma de pagamento: '))

if pagar == 1:
    print(f'Total: R$ {subtotal*0.9}')

elif pagar == 2:
    print(f'Total: R$ {subtotal*1.155}')

else:
    print('Código inválido')