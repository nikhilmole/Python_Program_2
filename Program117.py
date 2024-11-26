def CountCapital(str):

    iCount = 0
    index = 0
    length = len(str)

    while(index < length):
        if(str[index] >= 'A')and(str[index] <= 'Z'):

            iCount = iCount + 1

        index = index + 1

    return iCount

def main():

    print("Enter the String : ")
    Arr = input()

    iRet = CountCapital(Arr)
    print("The capital letteres are : ",iRet)

if __name__ == "__main__":
    main()