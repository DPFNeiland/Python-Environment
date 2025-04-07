from math import sqrt


while True:
    N = int(input())
    ehprimo = False

    if(N == 1):
        print('não eh primo')

    else:
        for i in range(2,int(sqrt(N)+1)):
            if(N%i == 0):
                print('não eh primo')
                ehprimo = True
                break
            
        if not ehprimo:
            print('eh primo')
            