def incn(n,k=1):
    """
    Prints strictly increasing n numbers using recursion
    """
    if n==0:
        return
    else:
        print(k)
        incn(n-1,k+1)
           

def main():
    n=int(input("Enter the value of n : "))
    incn(n)

if __name__=="__main__":
    main()