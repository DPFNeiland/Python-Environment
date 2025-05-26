
while True:
    try:
        x = int(input())
        
        if x >= 1:
            print('vai ter duas!')
        else:
            print('vai ter copa!')
    except EOFError:
        break