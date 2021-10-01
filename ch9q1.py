
import sys
import os


def copyf(file1,file2):
    '''
    Reads line by line from file1 and prints to file2 adding a new line
    '''
    f1=open(file1,"r")
    f2=open(file2,"w")
    line=f1.readline()
    while(line!=""):
        f2.write(line)
        f2.write("\n")
        line=f1.readline()
    f1.close()
    f2.close()


def main():
    #print(os.getcwd())
    #sys.path.append(r"C:\\Users\\Shashwat Ratna\\Desktop\\realshh\\Learn\\Python\\ch9_Files__Exceptions")
    #print(os.getcwd())
    file1=input("Enter file name to open :")
    file2=input("Enter name of file to be created :")
    copyf(file1,file2)

if __name__=="__main__":
    main()