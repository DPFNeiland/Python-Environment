
X = 1
M = 1

while (X!=0) or (M!=0):
    X, M = [int(i) for i in input().split()]
    if(X==0 and M == 0):
        break
    else:
        print(f'{X*M}')
