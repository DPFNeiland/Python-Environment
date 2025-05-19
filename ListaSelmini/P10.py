

# class Policial:
#     def __init__(self, nome):
#         self.nome = nome
#         self.ocorrencias = []

#     def adicionar_ocorrencia(self, tipo):
#         self.ocorrencias.append(tipo)

#     def contar_ocorrencias(self, tipo=None):
#         if tipo:
#             return sum(1 for ocorrencia in self.ocorrencias if ocorrencia == tipo)
#         return len(self.ocorrencias)


# # Inicialização dos policiais
# policiais = {
#     'Clancy': Policial('Clancy'),
#     'Eddie': Policial('Eddie'),
#     'Lou': Policial('Lou')
# }

# total_ocorrencias = 0
# homer_ocorrencias = 0
# direcao_perigosa_ocorrencias = 0

# def alocar_ocorrencia(tipo, gravidade):
#     global total_ocorrencias, homer_ocorrencias, direcao_perigosa_ocorrencias
#     total_ocorrencias += 1

#     # Ocorrência do tipo Homer
#     if tipo == 'Homer':
#         policiais['Clancy'].adicionar_ocorrencia(tipo)
#         homer_ocorrencias += 1
#         return

#     # Verificação de ocorrências do tipo Direção Perigosa
#     if tipo == 'Direção Perigosa':
#         direcao_perigosa_ocorrencias += 1

#     # Atribuição ao policial com menos ocorrências
#     menos_ocorrencias = min(policiais.values(), key=lambda p: len(p.ocorrencias))
#     menos_ocorrencias.adicionar_ocorrencia(tipo)


# def exibir_resumo():
#     print("\nResumo de Ocorrências:")
#     for policial in policiais.values():
#         print(f"{policial.nome}: {len(policial.ocorrencias)} ocorrências")
#     print(f"Ocorrências do tipo Homer: {homer_ocorrencias}")
#     if total_ocorrencias > 0:
#         percentual = (direcao_perigosa_ocorrencias / total_ocorrencias) * 100
#         print(f"Percentual de Direção Perigosa: {percentual:.2f}%")


# # Exemplo de uso
# alocar_ocorrencia('Direção Perigosa', 'Baixo')
# alocar_ocorrencia('Homer', 'Alto')
# alocar_ocorrencia('Bebedeira', 'Médio')
# alocar_ocorrencia('Barulho', 'Baixo')
# alocar_ocorrencia('Direção Perigosa', 'Alto')
# exibir_resumo()



ocorrencia = 1
qtdDeOcorrencia = -1

tipoDeOcorrencia = []
gravidadeDeOcorrencia = []

while ocorrencia != 0:
    
    qtdDeOcorrencia +=1
    
    print("Quer registrar uma ocorreêcia? ")
    ocorrencia = int(input("Digite 1 para sim e 0 para não: "))
    
    if ocorrencia == 0:
        break

    print(qtdDeOcorrencia)
    print("Que tipo de ocorrencia é?")
    print("1 - Direção Perigosa\n2 - Barulho\n3 - Bebedeira\n4 - Homer\n")
    tipoDeOcorrencia.append(int(input()))
    
    match tipoDeOcorrencia[qtdDeOcorrencia]:
        case 1:
            print("1 - Baixo\n2 - Médio\n3 - Alto")
            gravidadeDeOcorrencia.append(int(input("Digite a gravidade da ocorrência: ")))
        
        case 2:
            print("1 - Baixo\n2 - Médio\n3 - Alto")
            gravidadeDeOcorrencia.append(int(input("Digite a gravidade da ocorrência: ")))

        case 3:
            print("1 - Baixo\n2 - Médio\n3 - Alto")
            gravidadeDeOcorrencia.append(int(input("Digite a gravidade da ocorrência: ")))

        case 4:
            print("Toda ocorrência de tipo Homer é de alta gravidade")
            gravidadeDeOcorrencia.append(int(4))
            listaClancy = []



    
''' Chefe Clancy, Eddie e Lou '''


for i in range(0, qtdDeOcorrencia):
    print(gravidadeDeOcorrencia[i])

print("Ocorrência do chefe Clancy: ")
for i in range(0, qtdDeOcorrencia, 3):
    print(f"Ocorrência de tipo: {tipoDeOcorrencia[i]}    Gravidade: {gravidadeDeOcorrencia[i]}")

print("Ocorrência do chefe: ")    
for i in range(0, qtdDeOcorrencia, 3):
    print(f"Ocorrência de tipo: {tipoDeOcorrencia[i]}    Gravidade: {gravidadeDeOcorrencia[i]}")
    
print("Ocorrência do Lou: ")    
for i in range(0, qtdDeOcorrencia, 3):
    print(f"Ocorrência de tipo: {tipoDeOcorrencia[i]}    Gravidade: {gravidadeDeOcorrencia[i]}")
    