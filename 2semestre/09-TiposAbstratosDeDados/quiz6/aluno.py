
class Aluno:
    def __init__(self, nome: str) -> None:
        self.nome = nome
        self.notas: list[float] = []

class Turma:
    def __init__(self) -> None:
        self.alunos: dict[str, Aluno] = {}

    
    def registra_nota(self, nome: str, nota: float) -> None:
        
        
        
        if nome not in self.alunos:
            self.alunos[nome] = Aluno(nome)
        self.alunos[nome].notas.append(nota)



t = Turma()
t.registra_nota("Ana", 7.0)
t.registra_nota("Ana", 9.0)
print(len(t.alunos), t.alunos["Ana"].notas)