import sys

def oddcopyl(file1,file2):
    '''
    Copies every alternate line from file1, odd numbered ones, to file2. 
    An attempt is made to handle all exceptions that can be possibly raised
    '''
    try:
        f1=open(file1,"r")
        f2=open(file2,"w")
    except IOError:
        print('Problem with opening the file');sys.exit()
    i=1
    line1=f1.readline()
    #lines=[]
    while(line1!=""):
        if(i%2!=0):
            try:
                f2.write(line1)
            except IOError:
                print('Problem with input or output');sys.exit()
        i=i+1
        line1=f1.readline()
    

    f1.close()
    f2.close()

def main():
    f1=input("Enter name of file to copy from : ")
    f2=input("Enter name of file to be created : ")
    oddcopyl(f1,f2)

if __name__=="__main__":
    main()
