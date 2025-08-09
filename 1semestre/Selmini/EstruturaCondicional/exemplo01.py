


M1 = float(input("Digite sua primeira nota: "))
M2 = float(input("Digite sua segunda nota: "))

MEDIA = (M1 + M2) / 2

print(f"Sua média é {MEDIA}")

if(MEDIA >= 0.0 and MEDIA < 4.0):
    print("Reprovado")
else:
    if(MEDIA >= 4.0 and MEDIA < 6.0):
        print("Exame")
        EX = float(input("Digite a nota do exame: "))
        if(EX >= 0.0 and EX < 6.0):
            print("Reprovado")
        else:
            if(EX >= 6.0 and EX <= 10):
                print("Aprovado")
            else:
                print("Nota inválida")
    else:
        if(MEDIA >= 6.0 and MEDIA <= 10.0):
            print("Aprovado")
        else:
            print("Nota inválida")