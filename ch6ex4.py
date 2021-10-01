def caser(s):
    '''
    first letter is made upper case
    others of small case
    without using in-built function
    but used lower() and upper()
    '''
    ans=""
    l=len(s)
    for i in range(0,l):
        if (s[i-1]==' ' or i==0) and s[i]!=' ' :
            if s[i] in "abcdefghijklmopqrstuvwxyz":
                ans+=s[i].upper()
        else:
            if s[i] in "ABCDEFGHIJKLMOPQRSTUVWXYZ":
                ans+=s[i].lower()
            else:
                ans+=s[i]
    return ans


def main():
    s=input("Enter a sentence : ")
    s=caser(s)
    print(s)

if __name__=="__main__":
    main()


            