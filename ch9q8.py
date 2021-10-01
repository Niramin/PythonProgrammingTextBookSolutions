def percentage(marks,total):
    try:
        percent=(marks/total)*100
    except ValueError:
        print('ValueError')
    except TypeError:
        print('TypeError')
    except ZeroDivisionError:
        print('ZeroDivisionError')
    except:
        print('Some other error')
    else:
        print(percent)
    finally:
        print("Function percentage completed")

def main():
    percentage(150.0,200.0)
    percentage(150.0,0.0)  
    percentage('150.0','200.0')

if __name__=="__main__":
    main()  