

def f(x):
    if x == 1: return -x
    return -5 * f(x - 1) + x

print(f(4))