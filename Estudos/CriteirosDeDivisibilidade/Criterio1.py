

def DividirPorX(X: int):
    if  int(N[len(N) - 1]) == X:
        return True
    else:
        return False


N = str(input())
resp = ""

if int(N[len(N) - 1]) % 2 == 0:
    resp += "S\n"
else:
    resp += "N\n"

sum = 0
for str in N:
    sum += int(str)

if sum % 3 == 0:
    resp += "S\n"
else:
    resp += "N\n"

if int(N[len(N) - 1]) % 5 == 0:
    resp += "S"
else:
    resp += "N"

print(resp)