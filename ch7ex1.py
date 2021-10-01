def rmduplicateslist(n):
    '''
    takes a list of values as paramter and returns another list without any
    duplicates
    '''
    n= set(n)
    return list(n)

def main():
    l=[1,2,2,3,3,3,4,"Hello"]
    print(rmduplicateslist(l))

if __name__=="__main__":
    main()
