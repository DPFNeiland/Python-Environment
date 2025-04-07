from math import sqrt


n = int(input())

resp = 1

for i in range(2,n+1):
    
    resp += sqrt(i)
    
print(resp)