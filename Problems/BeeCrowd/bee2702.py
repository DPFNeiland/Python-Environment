
Ca, Ba, Pa = [int(i) for i in input().split()]

Cr, Br, Pr = [int(i) for i in input().split()]

resp = 0

if(Ca-Cr<0):
    resp += abs(Ca - Cr)
    
if(Ba-Br<0):
    resp += abs(Ba - Br)
    
if(Pa-Pr<0):
    resp += abs(Pa - Pr)

print(f'{resp}')