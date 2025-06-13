



A = int(input())
B = int(input())
C = int(input())
D = int(input())

atual = C

resp = "S"

while not ( A <= atual and atual <= B):
    if atual < A:
        resp = "N"
        break  
    atual -=D
    
print(resp)