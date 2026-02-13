def passadas():
    N = int(input())

    for _ in range(N):
        texto = input()
        
        mensagem = ""
        for c in texto:
            if c.isalpha():
                mensagem += chr(ord(c) + 3)
            else:
                mensagem += c

        mensagem = mensagem[::-1]
        
        meio = len(mensagem) // 2
        cesar = ""
        for i in range(len(mensagem)):
            if i < meio:
                cesar += mensagem[i]
            else:
                cesar += chr(ord(mensagem[i]) - 1)

        print(cesar)

def main():
    passadas()

if __name__ == "__main__":
    main()
