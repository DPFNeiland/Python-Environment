
maxi = 999
array = [6,2,5,1,7,4,8,3]
value = [-1] * (len(array))
ready = [False] * (len(array))

def solve(n: int):
    if n == 0:
        return 1
    
    if ready[n]:
        return value[n]
    
    for i in range(len(array)):
        if array[n] > array[i]:
            value[n] = max(value[n],solve(i) + 1)        
    ready[n] = True
    
    return solve(n-1)


def main():
    solve(len(array)-1)
    print(value)
    
    
if __name__ == "__main__":
    main()