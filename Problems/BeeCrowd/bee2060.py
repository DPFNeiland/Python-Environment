








N = int(input())

list = list(map(int,input().split()))

multiplo2 = 0
multiplo3 = 0
multiplo4 = 0
multiplo5 = 0

for i in range(0,N):
    
    if(list[i]%2 == 0):
        multiplo2 += 1
    
    if(list[i]%3 == 0):
        multiplo3 += 1
    
    if(list[i]%4 == 0):
        multiplo4 += 1
        
    if(list[i]%5 == 0):
        multiplo5 += 1
        
print(f'{multiplo2} Multiplo(s) de 2')
print(f'{multiplo3} Multiplo(s) de 3')
print(f'{multiplo4} Multiplo(s) de 4')
print(f'{multiplo5} Multiplo(s) de 5')