
def minhaFuncaoDoritos(x, y):
    resultado = []
    for i, (a, b) in enumerate(zip(x, y)):
        if i % 2 == 0:
            resultado.append((a + b,))
        else:
            resultado.append((a*b, a- b))

    return tuple(resultado)

t1 = {1, 2, 3, 4, 5}
t2 = {6, 7, 8, 9, 10}

print(minhaFuncaoDoritos(t1, t2))