

def minhaFuncao(n):
    if n < 4: return 3 * n
    return 2* minhaFuncao(n - 4) + 5

print(minhaFuncao(3) + minhaFuncao(7))