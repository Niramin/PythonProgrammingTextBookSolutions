def ghk(a,b,n,k1=0,p=0):
    '''
    a is a string 
    b is a string
    n is the length of (a+b)
    '''
    
    a.insert(p,b[k1])
    
    if len(a)==n:
        print(a)
    else:
        ghk(a,b,n,k1+1,p+1)
    
    a.remove(b[k1])

    if p<k1:
        ghk(a,b,n,k1,p+1)

    

def main():
    a="A B"
    b="C D"
    a=a.split()
    b=b.split()
    n=len(a)+len(b)
    ghk(a,b,n)
    

if __name__=="__main__":
    main()
