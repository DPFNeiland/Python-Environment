t = int(input())

for _ in range(t):
    
    n, m = map(int, input().split())
    
    print(f"{((n)//3)*((m)//3)}")