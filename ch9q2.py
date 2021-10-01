def wordsf(file1):
    '''
    Takes file and displayes no. of words in it
    '''
    f=open(file1,"r")
    lines=f.read()
    lines=lines.split()
    f.close()
    return len(lines)


def main():
    n=input("Enter name of file : ")
    print(wordsf(n))

if __name__=="__main__":
    main()