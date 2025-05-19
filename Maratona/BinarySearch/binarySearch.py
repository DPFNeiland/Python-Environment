
def binary_search(sequence, item):
    begin_index = 0
    end_index = len(sequence) - 1
    
    while begin_index <= end_index:
        midpoint = begin_index + (end_index - begin_index) // 2
        midpoint_value = sequence[midpoint]
        if midpoint_value == item:
            return midpoint
        
        elif item < midpoint_value:
            end_index = midpoint - 1
            
        else:
            begin_index = midpoint + 1
            
    return None



lista = [10,9,8,5,3,7,92,185,78,1,0,65]
# lista = [0, 1, 3, 5, 7, 8, 9, 10, 65, 78, 92, 185]

ista = [10,9,8,5,3,7,92,185,78,1,0,65]

def mergeSort(alist):
    print("Spliting ", alist)
    
    if len(alist) > 1:
        mid = len(alist)//2
        lefthalf = alist[:mid]
        righthalf = alist[mid:]
        
        mergeSort(lefthalf)
        mergeSort(righthalf)
        
        i = 0
        j = 0
        k = 0
        
        while i < len(lefthalf) and j < len(righthalf):
            if lefthalf[i] < righthalf[j]:
                alist[k] = lefthalf[i]
                i = i + 1
                
            else:
                alist[k] = righthalf[j]
                j = j + 1
            
            k = k + 1
            
        while i < len(lefthalf):
            alist[k] = lefthalf[i]
            i = i + 1
            k = k + 1
            
        while j < len(righthalf):
            alist[k] = righthalf[j]
            j = j + 1
            k = k + 1
        
        print("Merging", alist)
        
mergeSort(lista)



item = int(input("Digite qualquer valor da lista: "))
print(binary_search(lista, item))