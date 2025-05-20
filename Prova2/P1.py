
from math import log

pA = 0
pB = 0

tA = 0
tB = 0 

t = 1

while pA >= pB:
    print("Segundo o enunciado, a população de A é menor que B")
    pA = float(input("Digite a população de A (em milhares): "))
    pB = float(input("Digite a população de B (em milhares): "))

while tA <= tB:
    print("Também no enunciado, a taxa de crescimento de A é maior que a de B")
    tA = float(input("Digite a taxa de crescimento de A (em milhares de habitantes / ano e em %): "))
    tB = float(input("Digite a taxa de crescimento de B (em milhares de habitantes / ano e em %): "))


print(f"A quantidade de anos necessária para que a cidade A ultrapasse B em números de habitantes é de aproximademente {log(pA/pB,(1+tB/100)/(1+tA/100)):.2f} ano(s)")


while pA * (1 + tA/100) < pB * (1 + tB/100):
    pA *= (1 + tA)
    pB *= (1 + tB)
    
    t+=1
    
print(f"A quantidade de anos necessária para que a cidade A ultrapasse B em números de habitantes é de {t} ano(s) arrendondados")


