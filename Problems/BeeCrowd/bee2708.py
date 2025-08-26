def debug(x):
    print(f'Variável: {x}')



jeeprestantes = int(0)
pessoasrestantes = int(0)

jeep = "ESPM"

while True:
    todo = input()
    
    
    if todo == "ABEND":
        break
    
    jeep, pessoas = todo.split()
    
    if jeep == "SALIDA":
        jeeprestantes += int(1)
        pessoasrestantes += int(pessoas)
    
    if jeep == "VUELTA":
        jeeprestantes -= int(1)
        pessoasrestantes -= int(pessoas)        
        
        if jeeprestantes < 0:
            jeeprestantes = 0
            
print(pessoasrestantes)
print(jeeprestantes)