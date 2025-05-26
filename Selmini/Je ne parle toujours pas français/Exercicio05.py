# BINARIOOOOOOOO

bin = 2
binario = False

while not binario:

    bin = (input("Digite um número binário: "))
    
    binario = True
    
    for i in bin:
        if int(i) != 1 and int(i) != 0:
            binario = False
            print("Digite um número binário válido!!!", end=" ")
            break
        else:
            binario= True


cont = len(bin)-1
binNum = 0
for i in bin:
    binNum += 2**cont*int(i)
    cont-=1

print(binNum)

