

def minhaFuncao(n):
    for i in range(2, n + 1):
        if n == i:
            return True
        elif n % i == 0:
            return False
        

for i in range(3, 7):
    print(i, minhaFuncao(i))