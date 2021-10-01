import sys
def pww(fprice,fweight):
    '''
    Takes the file containing price and the file containing weight
    and writes another file that contains the price per weight of 
    those items
    '''
    try:
        fp=open(fprice,"r")
        fw=open(fweight,"r")
        fpww=open("PricePerWeight","w")
    except IOError:
        print("Problem in opening required files");sys.exit()
    price=[]
    item=[]
    line1=fp.readline()
    while(line1!=''):
        k=line1.split()
        #print(k)
        try:
            price.append(int(k[-1]))
            itemname=""
            for i in k[0:-2]:
                itemname+=i+" "
            item.append(itemname)
        except TypeError:
            print("failed converting string price to int price or\
                the lesser likely scenario of having failed to append");sys.exit()
        line1=fp.readline()
    weight=[]
    line1=fw.readline()
    while(line1!=''):
        k=line1.split()
        #print(k)
        try:
            weight.append(int(k[-1]))
        except TypeError:
            print("failed converting string weight to int price");sys.exit()
        line1=fw.readline()
    
    for i in range(0,len(item)):
        try:
            fpww.write(item[i]+" : "+"%.2f"%(price[i]/weight[i])+"\n")
        except IOError:
            print("failed to write to new file fpww");sys.exit()
    fp.close()
    fw.close()
    fpww.close()

def main():
    pww("price","weight")

if __name__=="__main__":
    main()
