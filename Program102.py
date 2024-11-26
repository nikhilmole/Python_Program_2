def Max(Arr, iLength):

    iMax = Arr[0]

    for i in range(iLength):
        if(iMax < Arr[i]):
            iMax = Arr[i]

    return iMax

def main():

    print("How many numbers you want to add in array : ")
    iSize = int(input())

    P = []

    print("Enter the numbers : ")
    for i in range(iSize):
        iNo = int(input())
        P.append(iNo)

    iRet = Max(P, iSize)
    print("The MAximum is : ",iRet)

if __name__ == "__main__":
    main()