def summer(l):
    """
    returns the cumulative sum of list elements till that index
    """
    for i in range(0,len(l)):
        print(sum(l[0:i+1]))
    
def main():
    k=[1,2,3,4,5,6,7,8,9,10]
    summer(k)

if __name__=="__main__":
    main()