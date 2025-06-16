

def misterio(a, b,c):
    r = 0
    i = c
    while i > 0:
        for j in range(0,c):
            if a[i] == b[j]:
                r+=1
                
        i -= 1
    return r

x = [12,74,87,29,37,34,50,19,23,56]
y = [14,53,23,62,12,56,42,97,71,60]

print(misterio(x,y,9))