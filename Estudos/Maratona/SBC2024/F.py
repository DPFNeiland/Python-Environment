






N = int(input())

a = 1
b = 1
for i in range(N):
    a,b = b, a
    b+=a
print(a)


