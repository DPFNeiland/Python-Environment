



NC = int(input())

for i in range(1, NC + 1):
    n, k = map(int, input().split())
    res = 0 
    for j in range(2, n + 1):
        res = (res + k) % j
    print(f"Case {i}: {res + 1}")  
