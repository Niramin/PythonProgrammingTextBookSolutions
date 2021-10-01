def stringer(n):
    '''
    Takes string n adds * after every repetitive charachter and returns the modified string
    '''
    ans=""
    for i in n:
        if(n.count(i)>1):
            ans+=i+"*"
        else:
            ans+=i
    return ans

def main():
    str=input("Enter string : ")
    str=stringer(str)
    print(str)

if __name__=="__main__":
    main()