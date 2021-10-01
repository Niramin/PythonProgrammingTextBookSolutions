def digitstoletters(n):
    '''
    takes an integer and returns a string that is the name of the number in words
    '''
    d=dict()
    d={0:"Zero",1:"One",2:"Two",3:"Three",4:"Four",5:"Five",6:"Six",7:"Seven",8:"Eight",9:"Nine"}
    ans=""
    for i in str(n):
        ans+=d[int(i)]+" "
    return ans
def main():
    x=int(input("Enter a Number :"))
    print("You entered : ",digitstoletters(x))
if __name__=="__main__":
    main()
