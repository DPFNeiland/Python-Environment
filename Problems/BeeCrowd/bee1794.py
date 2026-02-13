




N = int(input())

LA, LB = input().split()

SA, SB = input().split()

if (int(LA) <= N) and (int(LB) >= N) and (int(SA) <= N) and (int(SB) >= N):
    print('possivel')

else:
    print('impossivel')