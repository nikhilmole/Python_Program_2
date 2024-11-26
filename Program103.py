def Min(Arr,iLength):

    iMin = Arr[0]

    for i in range(iLength):
        if(iMin > Arr[i]):
            iMin = Arr[i]

    return iMin
def main():

    print("How many numbers you want to add in array : ")
    iSize = int(input())

    P = []

    print("Entee the numbers : ")

    for i in range(iSize):
        iNo = int(input())
        P.append(iNo)
    
    iRet = Min(P, iSize)
    print("The minimum number is : ",iRet)

if __name__ == "__main__":
    main()