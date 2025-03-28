def mdc(X,Y):
    resto = float(0)
    aux = int(0)

    while (resto) or aux == 0:
        resto = X%Y
        X = Y
        Y = resto
        aux =+ 1
        
    return X   



while True:
    try:
        X, Y = [float(i) for i in input().split()]        
        
        print(f'{(2*X+2*Y)/mdc(X,Y):.0f}')      

    except EOFError:
        break