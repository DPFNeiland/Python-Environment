
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
    posfixa = ""  

    for ch in expressao:
        if ch != " ":
            if ch in ("+", "-", "*", "/", "%", "^"):
                while pilha and (prioridade(pilha[-1]) >= prioridade(ch)):
                    posfixa += pilha.pop()
                pilha.append(ch)
            
            elif ch == "(":
                pilha.append(ch)

            elif ch == ")":
                while pilha[-1] != "(":
                    posfixa += pilha.pop()
                
            else:
                posfixa += ch

    # Esvazia toda a pilha caso tenha sobrado alguma objeto
    while pilha:
        posfixa += pilha.pop()

    return posfixa
# programa principal
expressao = input("Informe a expressão infixa: ")
posfixa = converter(expressao)

print(posfixa)
