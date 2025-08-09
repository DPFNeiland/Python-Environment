

N = int(input())

for i in range (0,N):

    aux = int(input())

    i = 1
    while True:

        if aux - i      > 0:
            aux= aux - i
            i = i + 1
        else:
            break
    print(i)