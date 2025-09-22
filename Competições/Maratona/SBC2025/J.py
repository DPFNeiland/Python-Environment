


provas = list(map(int, input().split()))

resp = 4
nivel = []

for i in range(10):
    if not provas[i] in nivel:
        nivel.append(provas[i])
        resp -= 1
        
print(resp)