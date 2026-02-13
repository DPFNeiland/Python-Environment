
k = int(input())

while k != 0:
    
    x, y = map(int, input().split())
    for _ in range(k):
        n, m = map(int, input().split())
        
        
        if n > x:
            if m > y:
                print("NE")
            elif m < y:
                print("SE")
            else:
                print("divisa")
            
        elif n < x:
            if m > y:
                print("NO")
            elif m < y:
                print("SO")
            else:
                print("divisa")
        
        else:
            print("divisa")
            
    k = int(input())
    