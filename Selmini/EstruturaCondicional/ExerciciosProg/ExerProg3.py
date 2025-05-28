

a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))
c = int(input("Digite o terceiro número:"))

if(a == b == c) or a == b or a == c or b == c :
    print("Existem valores iguais")
elif a < b and a < c:
    print(f"{a} é o menor valor")
elif b < a and b < c:
    print(f"{b} é o menor valor")
elif c < a and c < b:
    print(f"{c} é o menor valor")
    
# print(f'{  'Olá' if(a == b) else "Fkanebg"}')