from random import randint
from math import inf

def deslocar_1 (v: list) -> list:
    v.reverse()
    v.append(v[0])
    v.reverse()
    v.pop()
    
    return v

v = [randint(0, 10) for i in range(10)]
k = int(input())
k =  k % len(v) 

print(v)


for i in range(k):
    v = deslocar_1(v)
    
print(v)