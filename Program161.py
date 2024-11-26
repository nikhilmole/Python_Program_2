i = 1

def Display(iNum):
    global i

    if(iNum < 0):

        iNum = -iNum

    if(i <= iNum):

        print(i,end='\t')

        i+=1

        Display(iNum)

def main():

    print("Enter the Number : ")
    iNo = int(input())

    Display(iNo)

if __name__ == "__main__":
    main()