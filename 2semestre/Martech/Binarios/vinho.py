import random

def descobrir(n, garrafa_envenenada):
    k = n.bit_length()
    testadores = [0] * k

    for i in range(k):
        if garrafa_envenenada & (1 << i) != 0:
            testadores[i] = 1
            
    # converter
    resp = 0
    for i in range(k):
        if testadores[i] == 1:
            resp |= (1 << i)
    
    return resp

# programa principal
n = 100

for i in range(100):
    garrafa_envenenada = random.randint(0, n - 1)
    resultado = descobrir(n, garrafa_envenenada)
    print(f'garrafa envenenada: {garrafa_envenenada}')
    print(f'garrafa envenenada descoberta: {resultado}', end="\n\n")