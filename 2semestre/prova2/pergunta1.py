

def Reverter(risadaSemConsoante: str) -> str:
    
    risadaSemConsoanteInvertida = ""
    
    for i in range(len(risadaSemConsoante) -1, -1, -1):
        risadaSemConsoanteInvertida += risadaSemConsoante[i]
    
    return risadaSemConsoanteInvertida

def verificarPalindromo(risada: str) -> bool:
    semConsoante = ""
    
    for letra in risada:
        if letra.lower() == "a" or letra.lower() == "e" or letra.lower() == "i" or letra.lower() == "o" or letra.lower() == "u": 
            semConsoante+=letra
  
       
    if semConsoante == Reverter(semConsoante):
        return True
    return False
    
    

def main():
    risada =  str(input("Digite sua risada: "))
    
    if verificarPalindromo(risada):
        print("sim")
    else:
        print("não")

if __name__ == "__main__":
    main()