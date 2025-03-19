import sys


N, H = [int(x) for x in input().split()]

A = list(map(int,input().split()))
    
resp = 0
    
for i in A:
    if H >= i:
        resp+=1

print(resp)