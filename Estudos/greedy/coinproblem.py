
coins = [1,2,5,10,20,50,100,200]



def solve(n: int):

    atual, resp = 7, 0
    
    while True:
        if n < coins[atual]:
            atual -=1
        
        if n >= coins[atual]:
            resp+=1
            n-=coins[atual]

        if n == 0:
            return resp

        
        

def main():
    n = int(input())
    
    print(solve(n))
    
if __name__ == "__main__":
    main()