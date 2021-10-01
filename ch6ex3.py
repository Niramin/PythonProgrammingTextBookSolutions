def hmwords(s):
    '''
    returns the number of words in a sentence
    '''
    return len(s.split())

def main():
    s=input("Enter sentence: ")
    print("The no. of words in this sentence are : ",hmwords(s))
if __name__=="__main__":
    main()