

p, j1, j2, r, a = list(map(int,input().split()))

# p == 1: jogador 1 é par
# p == 0: jogador 1 é ímpar 

# j1 e j2: número escolhido por jogador1 e 2

# r == 1: jogador 1 roubou
# r == 0: jogador 1 não roubou

# a == 1: jogador 2 acusou
# a == 0: jogador 2 não acusou

if r == 1 and a == 1:
    print("Jogador 2 ganha!")
    
elif r == 0 and a == 1:
    print("Jogador 1 ganha!")
    
elif r == 1 and a == 0:
    print("Jogador 1 ganha!")
    
elif (j1+j2) % 2 == 0 and p == 1:
    print("Jogador 1 ganha!")
    
elif (j1+j2) % 2 == 1 and p == 0:
    print("Jogador 1 ganha!")
    
elif (j1+j2) % 2 == 0 and p == 0:
    print("Jogador 2 ganha!")
    
elif (j1+j2) % 2 == 1 and p == 1:
    print("Jogador 2 ganha!")