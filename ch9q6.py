def wf(Filename):
    '''
    Reads the file and returns the count( a dictionary) of,
    alphabets,
    blank spaces,
    lowercase letters,
    number of words starting with a vowel,
    number of occurences of the word "Beautiful",
    in the file.
    '''

    f1=open(Filename,"r")
    t=f1.read()
    count={"Alphabets" : 0,"Blank spaces":0,"Lowercase letters":0,"Uppercase letters":0,"No. of words starting with a vowel":0,\
        "No. of occurrences of the word 'Beautiful'":0}
    #t.replace("\n","")
    print(t)
    for i in t:
        if i==" ":
            count["Blank spaces"]+=1
        if i in "abcdefghijklmnopqrstuvwxyz":
            count["Lowercase letters"]+=1
        if i in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            count["Uppercase letters"]+=1
    l=t.split()
    print(len(l),l)
    for i in l:
        if i[0] in "aeiou":
            count["No. of words starting with a vowel"]+=1
        if i.lower()=="beautiful":
            count["No. of occurrences of the word 'Beautiful'"]+=1
    count["Alphabets"]= count["Lowercase letters"]+count["Uppercase letters"]
    f1.close()
    return count

def main():
        n=input("Enter file name :")
        t=wf(n)
        print(t)

if __name__=="__main__":
        main()