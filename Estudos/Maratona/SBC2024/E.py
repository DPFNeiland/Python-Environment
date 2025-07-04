N = int(input())
estojo = []
resp = 0

for i in range(N):
    estojo.append(list(map(int, input().split())))

importante = [estojo[0][0], estojo[0][ N - 1], estojo[ N - 1][ N - 1], estojo[ N - 1][0] ]
menor = importante[0]

for i in range(4):
    if menor > importante[i]:
        resp = i
        menor = importante[i]
         
print(resp)