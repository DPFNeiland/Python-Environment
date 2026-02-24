
from Professsor import Professor

def validar_input_int(variavel, texto) -> int:

    variavel = 0
    
    while variavel <= 0:
        variavel = int(input(texto))

    return variavel

def validar_input_float(variavel, texto) -> float:

    variavel = 0
    
    while variavel <= 0:
        variavel = float(input(texto))

    return variavel


# Desenvolva um programa em python que gere três objetos representando os 
# professores e, em seguida, imprima no vídeo o valor do salário bruto de cada 
# professor. A entrada dos dados para cada professor deverá ser realizada via teclado.

def cadastrar_professores() -> list[Professor]:
    ProfessorHoraAula = -1.0
    ProfessorNumeroAulasSemanais = -1.0

    professores = []
    qtdProfessores = int(input("Digite a quantidade de professores para cadastrar: "))

    for _ in range(qtdProfessores):
        print("-" * 50)
        ProfessorNome = str(input("Digite o nome do professor: "))
        ProfessorTitulo = str(input("Digite o título do professor: "))
        ProfessorHoraAula = validar_input_float(
                ProfessorHoraAula,
                "Digite a hora aula do professor: "
            )
        
        ProfessorNumeroAulasSemanais = validar_input_int(
            ProfessorNumeroAulasSemanais,
            "Digite o número de aulas do professor: "
        )

        professor = Professor(
            ProfessorNome,
            ProfessorNumeroAulasSemanais,
            ProfessorHoraAula,
            ProfessorTitulo
        )

        professores.append(professor)
    
    return professores


def imprimir_professores(professores: list[Professor]):

    print("Nome do professor | Salário bruto em R$")
    print("-" * 50)

    for professor in professores:

        print(f"{professor.nome:<18}", end="|")
        print(f"{ " R$ " + str(int(professor.calcular_salario()*100)/100)}")
