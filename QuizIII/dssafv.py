

n1 = int(input("Informe um valor "))
m = n1

print(m)

n2 = int(input("Informe outro valor "))
if n2 > m:
    m = n2

print(m)

n3 = int(input("Informe mais um valor "))
if n3 > m:
    m = n3

print(m)


if n1 == n2 and n2 == n3:
    print("essa combinação de valores não é desejada")
    print(m)
else:
    print(m)