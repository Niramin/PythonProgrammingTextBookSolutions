def anagrammer(n1,n2):
    '''
    Checks if the two entered strings are anagrams, returns boolean
    '''
    t=False
    if len(n1)==len(n2) :
        t=True
        for i in n1:
            if i not in n2 :
                t= False
    return t

def main():
    n1= input("Enter first to check for anagram :")
    n2=input("Enter second string :")
    ans=anagrammer(n1,n2)
    print("They are an anagram ? :",ans)

if __name__=="__main__":
    main()

