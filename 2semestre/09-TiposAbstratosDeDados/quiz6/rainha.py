
class Rainha:
    def __init__(self, n: int) -> None:
        self.n = n

def coroar(d: dict, k: Rainha) -> None:
    d['x'] = Rainha(k.n)
    d['y'] = k
    k.n = 20
    d['x'].n = k.n + 1
    k = Rainha(5)
    return d

k = Rainha(3)
d = {}
coroar(d, k)

print(d['x'].n)
print(d['y'].n)
print(k.n)