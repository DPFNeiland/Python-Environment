N = int(input())

S = str(input())

Valores = 'NLSO'
resp = 0

for i in S:

    if(i == 'D'):
        resp+=1

        if(resp >= 4):
            resp -= 4
    else:
        resp-=1
        if (resp < 0):
            resp += 4

    

    

print(Valores[resp])