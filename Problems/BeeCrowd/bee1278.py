

n = int(input())

while n != 0:
    strings = []
    width = -1
    
    for _ in range(n):
        aux = str(input())
        
        newAux = ""
        for i in range(len(aux) - 1):
            if not (aux[i] == " " and aux[i+1] == " "):
                newAux += aux[i]
        newAux += aux[i + 1]
        
        
        newAux = newAux.removeprefix(" ")
        newAux = newAux.removesuffix(" ")
        
        if width < len(newAux):
            width = len(newAux)
        
        strings.append(newAux)
    
    for i in range(n):
        print(f"{strings[i]:>{width}}")
    
    
    
    n = int(input())
    