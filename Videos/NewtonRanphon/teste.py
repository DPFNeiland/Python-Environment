


def calcular_funcao(x):
    return 4500000000000000000000000*x - 5400000000000000000000000

def derivada_da_funcao(x):
    return 4500000000000000000000000

def testar_newton(aprox):
    if aprox == 0:
        return 1
    
    x = testar_newton(aprox - 1)
    
    return x - calcular_funcao(x)/derivada_da_funcao(x)
    
    
print(f"x = 5 diz que é : {calcular_funcao(1)}")
print(f"x = 5 diz que é : {calcular_funcao(3)}")

print(f"x = 5 diz que é em sua derivada: {derivada_da_funcao(1)}")
print(f"x = 5 diz que é em sua derivada: {derivada_da_funcao(3)}")

print(f"Raiz da equção 2x-5 é : {testar_newton(998)}")