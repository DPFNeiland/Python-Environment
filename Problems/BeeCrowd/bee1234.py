

while True:
    try:
        mensagem = input()
        atual = True

        for i in range(len(mensagem)):
            if atual and mensagem[i].isalpha():
                print(mensagem[i].upper(),end="")
                atual = not atual
            elif mensagem[i].isalpha():
                print(mensagem[i].lower(),end="")
                atual = not atual
            else:
                print(mensagem[i],end="")
        
        print()
    except EOFError:
        break