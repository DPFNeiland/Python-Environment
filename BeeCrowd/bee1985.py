





N = int(input())

resp = 0

for i in range(0,N):
    P, Q = [int(x) for x in input().split()]
    resp += (P%1000*1+0.50)*Q

print(f'{resp:.2f}')