


N = int(input())

for i in range(0,N):
    Str = str(input()).lower()
    resp = 1

    for char in Str:
        
        if (char == 'a') or (char == 'e') or (char == 'i') or (char == 'o') or (char == 's'):
            resp = resp * 3
        else:
            resp = resp *2
            
    print(resp)