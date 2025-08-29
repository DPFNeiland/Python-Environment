
# função criptografar
def cripografar(text: str, gap: int) -> str:
    aux = ""
    for letter in text:
        if letter.isalpha():
            code = ord(letter)
            aux += chr((code - 97 + gap)%26 + 97)
        else:
            aux += letter
            
    return aux

def descripografar(text: str, gap: int) -> str:
    aux = ""
    for letter in text:
        if letter.isalpha():
            code = ord(letter)
            aux += chr((code - 97 - gap)%26 + 97)
        else:
            aux += letter
            
    return aux

# função principal:
def main():
    texto = input("Informe uma frase: ").lower()
    deslocamento = int(input("Deslocamento: "))
    texto_cripto = cripografar(texto, deslocamento)
    print(texto_cripto)
    
    texto_cripto = descripografar(texto_cripto, deslocamento)
    print(texto_cripto)

# programa principal
if __name__ == "__main__":
    main()