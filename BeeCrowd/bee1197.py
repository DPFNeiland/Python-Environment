



while True:
    try:
        N1, N2 = (input().split())
        
        print(f'{int(N1)*int(N2)*2}')
        
    except EOFError: 
        break