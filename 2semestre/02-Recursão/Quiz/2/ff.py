

def ff(n, ind):
    for i in range(ind):
        print(' ')
        
    print(f"ff{n}, {ind}")
    if n == 1: return 1
    if n % 2 == 0: return ff(n // 2, ind + 1)
    return ff((n-1) // 2, ind + 1) + ff((n + 1) // 2, ind + 1)

print(ff(3, 2))