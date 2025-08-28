

N = int(input())

for i in range(0,N):

    K = int(input())

    for j in range(0,K):

        feed = int(input())

        if(feed == 1):
            print('Rolien')
        elif(feed == 2):
            print('Naej')
        elif(feed == 3):
            print('Elehcim')
        else:
            print('Odranoel')