


    


def main():
    fatorial = [1] * (10**5 + 1)
    MOD = 1000000009

    for i in range(4,100001):
        fatorial[i-3] = (fatorial[i-4]*i ) % MOD 
        
    while True:
        n = int(input())
        
        if n == 0:
            break
        
        print(fatorial[n - 3])

if __name__ == "__main__":
    main()