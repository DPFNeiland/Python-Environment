
'''
    Dado duas relações de Timões e dado o valor N adquirido pelo joalheiro,
    mostre no terminal quanto deve ser pago ao taverneiro
    o rB1 > rA1 & rB2 > rA2
'''

resp = 0

rA1, rA2 = map(int, input().split())
rB1, rB2 = map(int, input().split())
n = int(input())

aux = n//rB1
resp += aux*rB2
n -= rB1*aux

aux = n//rA1
resp += aux*rA2
n -= rA1*aux

resp += n*(rB2-rA2)/(rB1-rA1)

print(resp)