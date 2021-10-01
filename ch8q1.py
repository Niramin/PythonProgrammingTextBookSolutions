def multiplication(a,b,sum=0):
    if b==0:
        return sum
    else :
        sum+=a
        return multiplication(a,b-1,sum)

                        

def main():
    a=int(input("Enter first number : "))
    b=int(input("Enter second number : "))
    c=multiplication(a,b)
    print("The product of the two numbers is:",c)

if __name__=="__main__":
    main()