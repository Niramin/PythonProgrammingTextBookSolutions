def counter(s):
    '''
    Counts number of words
    '''
    ans=0
    l=len(s)
    for i in range(0,l):
        if (s[i-1]==' ' or i==0) and s[i]!=' ' :
            ans=ans+1
    return ans


def main():
    s=input("Enter a sentence : ")
    s=counter(s)
    print(s)

if __name__=="__main__":
    main()
