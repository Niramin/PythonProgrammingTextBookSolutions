def hanoi(n,source,spare,target):
    if n==1:
        print("Transfer 1 pebble from "+ source+ " to "+target)
    elif n==0:
        return
    else:
        hanoi(n-1,source,target,spare)
        print("Transfer 1 pebble from "+source +" to "+ target)
        hanoi(n-1,spare,source,target)

    


def main():
    n=int(input("Enter number of pebbles or stones for Tower of Hanoi Problem:"))
    hanoi(n,"Pole 1","Pole 2","Pole 3")

if __name__=="__main__":
    main()