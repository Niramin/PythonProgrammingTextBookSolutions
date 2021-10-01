def permute(lst1,op=set(),lst2=[],k=0,pos=0):
    """
    Supposed to print all possible permuations of lst1
    """
    lst2.insert(pos,lst1[k])
    if len(lst2)==len(lst1):
        op.add("".join(lst2))
    else:
        permute(lst1,op,lst2,k+1,pos)
    lst2.remove(lst1[k])

    if pos< k:
        permute(lst1,op,lst2,k,pos+1)


def bins(n):
    s=""
    t=set()
    for i in range(0,n+1):
        s="0 "*i +"1 "*(n-i)
        s=s.split()
        permute(s,t)
    return t





                
 
def main():
    n=int(input("Enter length of strings : "))
    m=bins(n)
    for i in m:
        print(i)



if __name__=="__main__":
    main()
   
