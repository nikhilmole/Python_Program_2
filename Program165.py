i = 1

def Display(iNum):
    global i

    if(iNum < 0):

        iNum = -iNum
    
    if(i <= iNum):

        print(i,"\t","*",end='\t')

        i += 1

        Display(iNum)

def main():

    print("Enter the number : ")
    iNo = int(input())

    Display(iNo)

if __name__ == "__main__":
    main()