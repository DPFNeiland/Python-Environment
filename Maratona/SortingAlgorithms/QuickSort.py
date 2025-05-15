

# Detailed look at how Quick sort works

# Big Oh analysis of running time

# Python Quick Sort code


# QuickSort is recursive (method that calls itself)

# Divide-and-Conquer algorithm

# Very efficient for large data set

# Worst case is O(n²)

# Average case is O(n log n).

# Perfomance depends largely on Pivot Selection

def partition(array, low, high):
    pivot = array[high]
    i = low - 1
    
    for j in range(low, high):
        if array[j] <= pivot:
            i = i + 1
            array[i], array[j] = array[j], array[i]
            
    array[i + 1], array[high] = array[high], array[i + 1]
    
    return i + 1

def quickSort(array, low, high):
    if low < high:
        pi = partition(array, low, high)
        
        quickSort(array, low, pi - 1)
        
        quickSort(array, pi + 1, high)
        
data = [1, 7, 4, 1 , 10, 9, -2]
print("Unsorted Array")
print(data)
size = len(data)
quickSort(data, 0, size - 1)
print("Sortado Array in ordem ascendente")
print(data)