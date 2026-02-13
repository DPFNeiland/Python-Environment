aulas = ["A1", "A2", "A3", "A4", "A5"] 

presencas = { 
    "Ana":   ["P", "P", "F", "P", "P"], 
    "Bruno": ["P", "F", "F", "P", "F"], 
    "Carla": ["P", "P", "P", "P", "P"], 
    "Diego": ["F", "F", "P", "F", "P"] 
}


# a) Para cada aluno, calcule: 
# - total de presenças (P); 
# - total de faltas (F); 
# - percentual de presença (% de aulas assistidas).

def calcular_total_presença(chamada: dict) -> dict:
    
    por_aluno = {}
    
    for aluno, presenca in chamada.items():

        presencas = 0
        faltas = 0
        
        for dia in presenca:
            if dia == "P":
                presencas += 1
            else:
                faltas += 1

        por_aluno[aluno] = gerar_parte_por_aluno(presencas, faltas)

    return por_aluno


# b) Gere um dicionário por_aluno com as informações no formato: "Ana": {"P": 4, "F": 1, "perc": 
# 80.0, "situacao": "APROVADO"}. O aluno é considerado APROVADO se sua presença for ≥ 75%. 
def gerar_parte_por_aluno(presencas: int, faltas: int) -> dict:
    
    return {
        "P": presencas, 
        "F": faltas, 
        "perc": presencas/(presencas+faltas)*100,
        "situacao": "APROVADO" if presencas/(presencas+faltas) >= 0.75 else "REPROVADO"
    }


# c) Calcule e exiba: 
# - a aula com mais faltas (ex: "A2"); 
# - o aluno com maior presença; 
# -  o aluno com mais faltas; 
# - a média de presença da turma (em %).


def calcular_Aula_Mais_Faltada_turma(presencas: dict, aulas: list) -> list:
    
    faltasEmCadaAula = [0] * len(aulas)
     
     
    for presenca in presencas.values():
        for i in range(len(aulas)):
            if presenca[i] == "F":
                faltasEmCadaAula[i] += 1

    listaAulasFaltas = list(zip(aulas, faltasEmCadaAula))
    
    maiorFaltas = -1
    aulaMaisFaltada = []
    
    for aula, falta in listaAulasFaltas:
            
        if falta > maiorFaltas:
            maiorFaltas = falta
            aulaMaisFaltada = []
            
        if falta == maiorFaltas:
            aulaMaisFaltada.append(aula)
        
    
    return aulaMaisFaltada

def calcular_MaiorOuMenor_Aluno_presenca(por_aluno: dict, PF = "P") -> list:
    
    '''
        por_aluno: dict
        parte do relatório
        
        PF:
        sendo opcional, a variável  define se o usuário quer o aluno
        com mais presença "P" ou o aluno mais faltante "F"
    '''
    
    alunoComMaisPresenca = []
    maior = -1
    
    for aluno, parte_aluno in por_aluno.items():
        if parte_aluno.get(PF) > maior:
            maior = parte_aluno.get(PF)
            alunoComMaisPresenca = []
            
        if parte_aluno.get(PF) == maior:
            alunoComMaisPresenca.append(aluno)
        
    
    return alunoComMaisPresenca

def calcular_Media_Presenca_Turma(por_aluno: dict) -> float:
    
    presencasPorcentagem = 0
    cont = 0
    
    for aluno, presenca in por_aluno.items():

        presencasPorcentagem += presenca.get("P")/(presenca.get("F")+presenca.get("P"))*100
        cont += 1
    
    return presencasPorcentagem/cont

# d) O relatório final deve seguir o formato: 
# relatorio = { 
#   "por_aluno": {...}, 
#   "aula_mais_faltas": "...", 
#   "melhor_presenca": "...", 
#   "mais_faltas": "...", 
#   "presenca_media_turma": ... 
# } 
    
def gerar_relatorio_final(aulas: list, presencas: dict) -> dict:
    por_aluno = calcular_total_presença(presencas)
    
    return {
        "por_aluno": por_aluno,
        "aula_mais_faltas": calcular_Aula_Mais_Faltada_turma(presencas, aulas),
        "melhor_presenca": calcular_MaiorOuMenor_Aluno_presenca(por_aluno),
        "mais_faltas": calcular_MaiorOuMenor_Aluno_presenca(por_aluno, "F"),
        "presenca_media_turma": calcular_Media_Presenca_Turma(por_aluno)
    }


def main():    
    
    relatorio = gerar_relatorio_final(aulas, presencas)
    print(relatorio)
    
    
if __name__ == "__main__":
    main()