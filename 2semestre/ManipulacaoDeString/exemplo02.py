
from random import choice

def digitar_chute(chute = "") -> str:
    while not chute.isalpha():
        chute = input("Digite uma letra: ")
        chute = chute.upper()
        
        if not chute.isalpha() or len(chute) != 1:
            print("UMA letra mano. ", end=" ") 

    return chute

def jogar(palavra: str) -> bool:


    erros = 0
    tamanho = len(palavra)
    acertou = [False] * tamanho 
    
    while erros < 6:
        chute = digitar_chute()

        if chute in palavra:
            print("A palavra é", end=" ")
        
        else:
            erros += 1
            print(f"Você errou pela {erros}ª vez. ", end = "")
            
            if erros == 6:
                print("Você falhou")            
                break
            else:
                print("Tente denovo")
        
        for i in range(tamanho):                
            if acertou[i]:
                print(palavra[i], end=" ")
                
            elif chute == palavra[i]:
                print(chute, end=" ") 
                acertou[i] = True
                
            else:
                print("_", end=" ")

        print()
        
        if all(acertou):
            print("parabéns mana")
            break
    
    
def escolher_palavra(palavras: list) -> str:
    return choice(palavras)


def ler_palavras() -> list:
    palavras = []
    palavra = ""

    while palavra != "0" or len(palavras) == 0:
        palavra = str(input(f"Digite as palavras que entrarão na forca (digite '0' para finalizar a inserção): "))  
        
        palavra = palavra.upper()  
        
        if palavra != "0" and not palavra in palavras:
            palavras.append(palavra)
    
    print(palavras)

    return palavras

def main():
    banco = ler_palavras()
        
    palavra = escolher_palavra(banco)
        
    jogar(palavra)

if __name__ == "__main__":
    main()

