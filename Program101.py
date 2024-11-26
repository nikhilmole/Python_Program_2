def Product(Arr, iLength):

    iPro = 1

    for i in range(iLength):
        if(Arr[i] % 2 != 0):
            iPro = iPro * Arr[i]

    return iPro

def main():

    print("How many numbers you want to add in array : ")
    iSize = int(input())

    P = []

    print("Enter the numbers : ")
    for i in range(iSize):
        iNo = int(input())
        P.append(iNo)

    iRet = Product(P, iSize)
    print("The product is : ",iRet)

if __name__ == "__main__":
    main()