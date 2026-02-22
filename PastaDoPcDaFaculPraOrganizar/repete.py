

# l = [7,2,4,8,2,4]
# l = [3,1,1,8,5,3]
lista = [7,8,9,9,8,7]





def eu(l) -> int:
    resp = -1
    encontrou = True
    for i in range(1, len(l)):
        if encontrou:
            for j in range(i, 0, -1):
                if l[j] == l[j-1]:
                    encontrou = False
                    resp = l[j]
                    break
                elif l[j] > l[j-1]:
                    break
                else: 
                    l[j], l[j-1] = l[j-1], l[j]

    return resp

def main():
    eu(lista)
    
if __name__ == "__main__":
    main()