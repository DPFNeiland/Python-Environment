
def RootInt(ans: int, n: int) -> int:
    if ans * ans > n:
        return ans - 1
    
    return RootInt(ans + 1, n)


def main():
    n = int(input())

    print(RootInt(1, n))

if __name__ == "__main__":
    main()