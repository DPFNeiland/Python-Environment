
# Detailed look at how Mege Sort works

# Big Oh analysis of running time

# Python Merge Sort code



# MergeSort is recursive (method thtat calls itself)

# Divide-and-Conquer algorithm

# Very efficient forlage data sets



# Merge Sort does log n merge steps because each
# merge step doubles the list size.

# It does n work for each merge step because it
# must look at every item

# So it runs in O(n long n).


lista = [10,9,8,5,3,7,92,185,78,1,0,65]

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
print(lista)