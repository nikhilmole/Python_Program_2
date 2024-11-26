def Dif(Arr, iLength):
    iMax = Arr[0]
    iMin = Arr[0]

    for i in range(iLength):
        if(iMax < Arr[i]):
            iMax = Arr[i]

        elif(iMin > Arr[i]):
            iMin = Arr[i]

    Ans = iMax - iMin
    return Ans

def main():

    print("How many numbers you want to in array : ")
    iSize = int(input())

    P = []

    print("Enter the numbers : ")

    for i in range(iSize):
        iNo = int(input())
        P.append(iNo)

    iRet = Dif(P, iSize)
    print("The Diference of Maximum and minimum number is : ",iRet)

if __name__ == "__main__":
    main()