

alpha = "S"
N, K = input().split()

alphaLyn = input()
frase = input()

for carac in frase:
    if not (carac in alphaLyn):
        alpha = "N"
        break

print(alpha)