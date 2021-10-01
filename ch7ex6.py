def mulist(n):
    '''
    multiplication tables for 5 multiples for n numbers
    '''
    l=list()
    for i in range(1,n+1):
        kl=list()
        for k in range(1,6):
            kl.append(int(k*i))
        l.append(kl)
    print(l)

def main():
    mulist(5)

if __name__=="__main__":
    main()