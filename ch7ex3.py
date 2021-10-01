def main():
    s=input("Enter a sentence : ")
    n=set(s)
    d={}#the dictionary
    for i in n:
        d.update({i:0})
        for k in s:
            if(i==k):
                d[i]=d[i]+1
    #print(d.items())
    for i in d:
        print(i+" : ",d[i])

if __name__=="__main__":
    main()



if __name__=="__main__":
    main()