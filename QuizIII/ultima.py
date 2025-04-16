




a = int(input(("Digite o primeiro valor:")))
b = int(input(("Digite o segundo valor:")))
c = int(input(("Digite o terceiro valor:")))


if a < b:
    aux = a
    a = b
    b = aux
    
if a < c:
    aux = a
    a = c
    c = aux
    
if b < c:
    aux = b
    b = c
    c = aux
    
    
print(f'{a} e {b} e {c}')