def OffBit(iNum):

    iResult = 0
    iMask = 0xFFFFFFBF

    iResult = iMask & iNum

    return iResult

def main():

    print("Enter the number : ")
    iNo = int(input())  

    iRet = OffBit(iNo)
    print("Updated number is : ",iRet)

if __name__ == "__main__":
    main()