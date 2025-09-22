

N = int(input())

binario = list(map(int, input().split()))

resp = 0
while len(binario) != 1:
    if binario[0] == 1 and len(binario) == 1:
        break
    
    if binario[len(binario) - 1] == 0:
        binario.pop()
        resp += 1
        
    else:
        binario10 = binario.copy()
        binario10.append(0)
        
        binario.reverse()
        binario.append(0)
        binario.reverse()

        novobin = []
        for i in range(len(binario)):
            if binario[i] == 1 and binario10[i] == 1:
                novobin.append(0)
            
            elif binario[i] == 1 or binario10[i] == 1:
                novobin.append(1)
                
            else:
                novobin.append(0)
        novobin.pop()
        novobin.append(0)
        
        binario = novobin.copy()
        resp+=1
                
print(resp)