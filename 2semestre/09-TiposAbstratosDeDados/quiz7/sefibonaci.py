

def sefi(n):
    if n == 1:
        return 1
    return (n-1)*sefi(n - 1)

print(sefi(4))
print(sefi(5))