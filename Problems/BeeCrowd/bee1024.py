

N = int(input())


for _ in range(N):
    texto = input()
    mensagem = ""
    for c in texto:
        if c.isalpha():
            aux = chr(ord(c)+3)
        else: 
            aux = c
        mensagem += (aux)
        
    invertido = ""
    
    
    for i in range(len(mensagem) - 1,-1,-1):
        invertido += mensagem[i]
        
    mensagem = invertido
    aux = (len(mensagem))//2
    
    cesar = ""
    for cchar in mensagem[0:aux]:
        cesar += cchar
    
    for cchar in mensagem[aux:len(mensagem)+1]:
        cesar += chr(ord(cchar)-1)
        
    print(cesar)