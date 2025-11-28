alunos = ["Ana", "Pedro", "Joana", "Lucas"]
notas = [85, 90, 92, 88]

def encontrar_melhor_alunos(alunos, notas):
    combinacao = zip(alunos, notas)
    return max(combinacao, key=lambda x: x[1])

print(encontrar_melhor_alunos(alunos, notas))