

def rio(x, y):
    if x == y or y == 0: return 1
    return rio(x - 1, y) + 1

print(rio(6, 2))