def permute(lst1,lst2=[],k=0,pos=0):
    """
    Supposed to print all possible permuations of lst1
    """
    lst2.insert(pos,lst1[k])
    if len(lst2)==len(lst1):
        print(lst2)
    else:
        permute(lst1,lst2,k+1,pos)
    lst2.remove(lst1[k])

    if pos< k:
        permute(lst1,lst2,k,pos+1)


