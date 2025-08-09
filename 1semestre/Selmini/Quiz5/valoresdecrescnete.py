

a = [0] * 10

a[0] = 0

for i in range(1, len(a)):
    a[i] = a[i - 1] + 1
    
print(a)