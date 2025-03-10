

prova1 = float(input("Digite a nota da primeira prova: "))
prova2 = float(input("Digite a nota da segunda prova: "))

trabalho1 = float(input("Digite a nota do primeiro trabalho: "))
trabalho2 = float(input("Digite a nota do segundo trabalho: "))

if((((prova1 + prova2)/2)*0.7+((trabalho1 + trabalho2)/2)*0.3)>=7):
    print("Aprovado!")
else:
    print("Reprovado")