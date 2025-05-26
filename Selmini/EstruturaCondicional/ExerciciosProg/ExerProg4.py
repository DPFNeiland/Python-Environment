
a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número: "))
c = int(input("Digite o terceiro número: "))

# a, b = min(a,b), max(a,b)

# b, c = min(b,c), max(b,c)

# a, b = min(a,b), max(a,b)

# print(f"Em ordem crescente: {a}, {b}, {c}") 

if a > b:
    aux = a
    a = b
    b = aux
    
if a > c:
    aux = a
    a = c
    c = aux
    
if b > c:
    aux = b
    b = c
    c = aux
    
print(f"Em ordem crescente: {a}, {b}, {c}") 