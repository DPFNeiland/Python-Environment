

while True:
    try:
        
        n1, n2 = input().split()

        n1 = int(n1)
        n2 = int(n2)

        print(abs(n1-n2))

    except EOFError:
        break