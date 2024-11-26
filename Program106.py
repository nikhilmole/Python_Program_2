def SumofDigits(Arr, iLength):
    iDigits = 0
    iSum = 0

    for i in range(iLength):
        iNo = Arr[i]
        iSum = 0
        
        while(iNo > 0):
            iDigits = iNo % 10
            iSum = iSum + iDigits
            iNo = iNo // 10

        print(iSum)


def main():

    print("How many numbers you want to add in array : ")
    iSize = int(input())

    P = []

    print("Enter the numbers : ")

    for i in range(iSize):
        iNo = int(input())
        P.append(iNo)
    
    SumofDigits(P, iSize)

if __name__ == "__main__":
    main()