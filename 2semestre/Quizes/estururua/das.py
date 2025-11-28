def processar(a):
    return tuple(x**2 if x % 2 == 0 else x for x in a)

print(processar((1,2,3,4)))