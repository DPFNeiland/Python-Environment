alunos = {
    "ana": {"matematica": 80, "fisica": 90},
    "pedro": {"matematica": 85, "fisica": 78, "quimica": 88},
    "joana": {"matematica": 92, "fisica": 88},
    "lucas": {"matematica": 76, "quimica": 95}
}

def melhores_em_disciplina(alunos, disciplina):
    melhor_aluno = None
    melhor_nota = -1
    for aluno, notas in alunos.items():
        if disciplina in notas and notas[disciplina] > melhor_nota:
            melhor_nota = notas[disciplina]
            melhor_aluno = aluno
    
    return melhor_aluno, melhor_nota

print(melhores_em_disciplina(alunos, "fisica"))