resp = str('N')

N = float(input())

A, L, P = [float(x) for x in input().split()]

if N <= A and N <= L and N <= P:
    resp = str('S')

print(resp)