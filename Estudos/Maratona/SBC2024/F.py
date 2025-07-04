


# A e B são coprimos se e somente se têm apenas um divisor comum
# em maior quantidade possível, que é igual a 1

# Então, mdc(a,b) == 1 <=> mdc(a+b, b) == 1 
# Tento até hoje deduzir isso...


N = int(input())

a = 1
b = 1
for i in range(N):
    a,b = b, a
    b+=a
print(a)


