

k = 0
fatorial = 1
i = 2
n = int(input())

while n != 0:

    if n < fatorial:
        n -= fatorial/(i-1)
        fatorial = 1
        i = 1
        k += 1

    if n == fatorial:
        n -= fatorial
        fatorial = 1
        i = 1
        k += 1

    fatorial *= i
    i += 1




print(k)