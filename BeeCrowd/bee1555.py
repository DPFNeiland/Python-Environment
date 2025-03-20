

N = int(input())

for i in range(0,N):
    x, y = [int(i) for i in input().split()]

    Rafael = (3*x)**2+ y**2
    Beto = 2*(x**2) +(5*y)**2
    Carlos = -100*x + y**3 

    if(Rafael > Beto) and (Rafael > Carlos):
        print("Rafael ganhou")
    elif(Beto > Rafael) and (Beto > Carlos):
        print("Beto ganhou")
    else:
        print("Carlos ganhou")