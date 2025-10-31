


def metodo(n):
    if n < 2: return n
    
    return metodo(n - 1) + metodo(n - 2) 

print(metodo(0))
print(metodo(1))
print(metodo(2))
print(metodo(3))
print(metodo(4))
print(metodo(5))
print(metodo(6))
print(metodo(7))
print(metodo(8))
print(metodo(9))
