
class Box:
    def __init__(self, size: int) -> None:
        self.size = size

def go(b1: Box, b2: Box) -> list[Box]:
    b1.size = 4
    ma = [b1, b2]
    return ma

if __name__ == "__main__":
    b1 = Box(5)
    ba = go(b1, Box(6))
    ba[0] = b1

    for i in range(len(ba)):
        print(ba[i].size)