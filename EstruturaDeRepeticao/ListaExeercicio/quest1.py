

lista = []


for i in range(0, 1000):
    
    aux = int(input(f"Digite o {i} valor: "))    
    
    lista.append(aux)
    
    if i == 0:
        mini = aux
        maxi = aux
        
    if mini > aux:
        mini = aux
    
    if maxi < aux:
        maxi = aux
        

print(f'Valor máximo: {maxi} \nValor mínimo: {mini}')