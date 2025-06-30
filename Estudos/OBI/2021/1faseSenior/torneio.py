


vit = 0

for i in range(6):
    x = input()
    
    if x == 'V':
        vit += 1
        
        
if vit == 1 or vit == 2:
    print("3")
    
elif vit == 3 or vit == 4:
    print("2")
    
elif vit == 5 or vit == 6:
    print("1")
    
else:
    print("-1")