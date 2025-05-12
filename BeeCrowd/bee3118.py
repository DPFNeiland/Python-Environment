
bacterias = "A"

segundos, regras = input().split()

segundos = int(segundos)
regras = int(regras)

coleta = {}

cultura = "atual"

for i in range(0,regras):
    antes, atual = input().split()
    
    coleta[antes] = atual
    
    
print(coleta)