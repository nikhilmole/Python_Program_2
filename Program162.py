i = 1

def Display(iNum):

    global i

    if(iNum < 0):
        iNum = -iNum

    if(iNum > 0):
    
        print(iNum,end='\t')
        iNum -= 1
        Display(iNum)
    

def main():

    print("Enter the Number : ")
    iNo = int(input())

    Display(iNo)

if __name__ == "__main__":
    main()