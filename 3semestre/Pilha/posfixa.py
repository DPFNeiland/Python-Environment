
from collections import deque



def prioridade(operador: str) -> int:
    match operador:
        case '(':
            return 1
        
        case '+' | "-":
            return 2

        case '/' | '*' | '%':
            return 3
        
        case '^':
            return 4
        
        case _:
            return 0
        

def converter(expressao: str) -> str:

    pilha = deque()
    polonesa = ""  

    for ch in expressao:
        if ch != " ":
            if ch in ("+", "-", "*", "/", "%"):
                pass


# programa principal
expressao = input("Informe a expressão infixa: ")
posfixa = converter(expressao)

print(posfixa)
