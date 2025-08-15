
def fatorial(n: int):
    return n*fatorial(n-1) if n != 0 else 1

def main():
    
    n = -1
    while not n >= 0: 
        n = int(input())
    
    print(fatorial(n))
    
        
if __name__ == "__main__":
    main()
