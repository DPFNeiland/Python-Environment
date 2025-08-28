

def count(ind: int):
    if ind == 0:
        return int(num[0])
    
    return int(num[ind]) + count(ind-1)


def main():
    global num 
    num = input()
    
    print(count(len(num)-1))


if __name__ == "__main__":
    main()