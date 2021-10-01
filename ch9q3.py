def writef(file1):
    '''
    Creates a file of sent name and writes data in it prompted by user 
    until nothing("") is entered
    '''
    f=open(file1,"w")
    print("Enter the data to be written :")
    t=input()
    m=""
    while(t!=""):
        t=t+"\n"
        m+=t
        t=input()
    f.write(m)
    print("The data has been entered!")
    f.close()

def main():
    n=input("Enter name of file to be created : ")
    writef(n)

if __name__=="__main__":
    main()
