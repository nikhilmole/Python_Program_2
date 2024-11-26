def Display(iNum):

    if(iNum > 0):

        print(iNum,end = '\t')

        iNum -= 1

        Display(iNum)

def main():

    print("Enter the Numbr : ")
    iNo = int(input())

    Display(iNo)

if __name__ == "__main__":
    main()