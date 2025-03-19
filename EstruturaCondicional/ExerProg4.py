

a = int(input("Digite o primeiro número:"))
b = int(input("Digite o segundo número:"))
c = int(input("Digite o terceiro número:"))

a, b = min(a,b), max(a,b)

b, c = min(b,c), max(b,c)

a, b = min(a,b), max(a,b)

print(f"Em ordem crecente: {a}, {b}, {c}")