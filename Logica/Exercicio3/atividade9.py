



numero3dig = int(input("Digite o número de 3 dígitos: "))

novo3digUnidade = numero3dig - numero3dig%100

novo3digCentena = (numero3dig - novo3digUnidade)%10

print(f"O valor invertido da ordem invertida é: {(novo3digCentena*100 + (numero3dig-(novo3digCentena)-novo3digUnidade) + novo3digUnidade/100):.0f}")