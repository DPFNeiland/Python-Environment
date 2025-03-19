


N = int(input())

for i in range(0,N):
    Nome, Forca = [str(x) for x in input().split()]
    
    if(Nome == 'Thor'):
        print('Y')
    else:
        print('N')