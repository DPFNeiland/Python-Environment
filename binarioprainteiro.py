


n = float(input())
# n = 18.7

n = n - int(n)

contador = 1

while contador < 5: 

    if (2 **( -contador) < n):
        print("1", end="")
        n = float(n - (2 **-contador))
    else:
        print("0", end="")

    contador += 1