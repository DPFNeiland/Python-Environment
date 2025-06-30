
# Detailed look at how Insertion Sort works

# Big Oh analysis of running time

# Python Insertion Sort code


# Insetion Sort que fiz

lista = [10,9,8,5,3,7,92,185,78,1,0,65]
    
print(lista)


for i in  range(1,len(lista)):
    
    for j in range (i  ,0 ,-1):
        
        if(lista[j - 1] > lista[j] ):
            lista[j], lista[j - 1] = lista[j - 1], lista[j]
            print(lista)
            

print((lista))

# Insertion Sort is not a fast sorting algorithm
# because it uses nested loops to sort

# It is useful only for small data sets

# It runs in O(n²)