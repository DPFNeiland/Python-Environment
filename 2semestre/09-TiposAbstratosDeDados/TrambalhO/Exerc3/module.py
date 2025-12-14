
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

def cadastrar_professores() -> list[Professor]:

    qtdProfessores = int(input("Digite a q"))