

n = int(input())

while n != 0:
    p1, p2 = 0, 0
    
    for _ in range(n):
        a, b = map(int, input().split())

        if a > b:
            p1 +=1
        elif a < b:
            p2 += 1
    
    print(f"{p1} {p2}")
    
    n = int(input())