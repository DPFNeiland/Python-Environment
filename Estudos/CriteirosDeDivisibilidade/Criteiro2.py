


# 4: últimos dois dígitos
# 9: soma dos dígitos = múltiplos de 9
# 25: útimos dois dígitos divisíveis por 25

N = input()

resp = ""
ultimo = len(N) - 1

# Divisível por 4

if int(N[ultimo])%2%2 == 0 and int(N[ultimo])%2 == 0:
    resp += "S\n"
else:
    resp += "N\n"

# Divisível por 9
sum = 0
for carac in N:
    sum += int(carac)

if sum % 9 == 0:
    resp += "S\n"
else:
    resp += "N\n"
    
# Divisível por 25

if int(N[ultimo])%5%5 == 0 and int(N[ultimo])%5 == 0:
    resp += "S"
else:
    resp += "N"

print(resp)