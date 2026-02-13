
from typing import List

class Professor:
    def __init__(self, nome: str):
        self.nome = nome


class Aluno:
    def __init__(self, nome: str, escolaridade: str):
        self.nome = nome
        self.escolaridade = escolaridade


class Sessao:
    def __init__(
            self, 
            professor: Professor, 
            aluno: Aluno,
            valor: float
        ):
        self.professor = professor
        self.aluno = aluno
        self.valor = valor


# a) gere três listas (uma para professores, outra para alunos e outra para sessão). Os dados devem ser inseridos via terminal e a 
# quantidade deverá ser informada pelo usuário. Os dados presentes na lista sessão são os mesmos dados dos professores e alunos 
# armazenados na lista de alunos e de professores.

def CadastrarProfessor() -> List:
    print("-" * 50)

    Professores = list()
    
    Pro = int(input("Digite a quantidade de Professores: "))
    for _ in range(Pro):
        ProfessorNome = str(input("Digite o nome do Professor: "))
        Professores.append(
            Professor(ProfessorNome)
        )
    return Professores


def CadastrarAlunos() -> List:
    print("-" * 50)

    Alunos = list()
    
    Alu = int(input("Digite a quantidade de Alunos: "))
    for _ in range(Alu):
        AlunoNome = str(input("Digite o nome do aluno: "))
        AlunoEscolaridade = str(input("Digite a escolaridade do aluno: "))
        Alunos.append(
            Aluno(
                AlunoNome,
                AlunoEscolaridade
                )
        )
    return Alunos

def CadastrarSessoes(Professores: List[Professor], Alunos: List[Aluno]) -> List:
    print("-" * 50)
    Sessoes = list()
    qtdProfessores = len(Professores)
    qtdAlunos = len(Alunos)

    Ses = int(input("Digite a quantidade de Sessoes: "))

    print("Lista dos professores e seus ID's")
    for i in range(qtdProfessores):
        print(f"{int((i + 1)):<2f}: {Professores[i].nome}")

    print("Lista dos alunos e seus ID's")
    for i in range(qtdAlunos):
        print(f"{int(i + 1):<2f}: {Alunos[i].nome}")

    for _ in range(Ses):
        print("-" * 50)
        indiceProfessor = -1
        indiceAluno = -1
        
        while indiceProfessor < 0 or indiceProfessor > qtdProfessores: 
            indiceProfessor = int(input("Digite o ID do professor da Sessao: "))

        while indiceAluno < 0 or indiceAluno > qtdAlunos:
            indiceAluno = int(input("Digite o ID do aluno da Sessao: "))

        SessaoValor = float(input("Digite o valor da Sessao: ")) 

        Sessoes.append(
            Sessao(
                Professores[indiceProfessor - 1],
                Alunos[indiceAluno - 1],
                SessaoValor
            )
        )
    return Sessoes

# b) escreva uma função que receba como parâmetro a lista de sessões e imprima no terminal, para cada sessão, o nome do professor, 
# o nome do aluno e o valor da sessão. A impressão deve estar organizada para o entendimento dos dados.
def ImprimirSessao(Sessoes: list[Sessao]) ->  None:

    print(f"Professor{" " * 5}| Aluno{" " * 10}| Valor da Sessão (R$)")
    print("-" * 50)
    
    for sessao in Sessoes:
        print(f"{str(sessao.professor.nome):<14}", end="")
        print(f"| {str(sessao.aluno.nome):<15}", end="")
        print(f"| {str(sessao.valor)}")

# c) escreva uma função que receba como parâmetro a lista de sessões e imprima no terminal o valor total recebido com as sessões.
def CalcularTotalSessoes(Sessoes: list[Sessao]) -> float:
    total = 0.0

    for sessao in Sessoes:
        total += sessao.valor

    return total

# d) escreva uma função que receba como parâmetro a lista de sessões e o nome de um professor. A função deverá calcular e imprimir o 
# valor que o professor recebeu pelas sessões que atendeu.
def CalcularTotalProfessor(Sessoes: list[Sessao], nomeProfessor: str) -> float | str:
    encontrouProfessor = False
    valorGanho = 0.0

    for sessao in Sessoes:
        if sessao.professor.nome == nomeProfessor:
            encontrouProfessor = True
            valorGanho += sessao.valor

    return valorGanho if encontrouProfessor else "Professor Não Encontrado"

def main():
    Professores = CadastrarProfessor()
    Alunos = CadastrarAlunos()
    Sessoes = CadastrarSessoes(Professores, Alunos)

    ImprimirSessao(Sessoes)

    total = CalcularTotalSessoes(Sessoes)
    print(f"Total ganho das sessoes: R$~{total}")

    nomeProfessor = str(input("Digite o nome do professor que deseja saber quanto ganhou: "))

    print(CalcularTotalProfessor(Sessoes, nomeProfessor))

if __name__ == "__main__":
    main()

# * Exemplo de Entrada de Teste:
# 3
# Flávio
# Selmini
# Surjan
# 3
# Rodrigo
# Ensino Fundamental I
# Naohan
# Ensino Fundamental II
# Rodrigues
# Ensino Superior
# 9
# 1
# 1
# 10
# 1
# 2
# 20
# 1
# 3
# 30
# 2
# 1
# 40
# 2
# 2
# 50
# 2
# 3
# 60
# 3
# 1
# 70
# 3
# 2
# 80
# 3
# 3
# 90
# Selmini
