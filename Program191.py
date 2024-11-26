def OffBit(iNum, iPos):

    iMask = 0
    iResult = 0

    iMask = ~(1 << (iPos - 1))

    iResult = iMask & iNum

    return iResult

def main():

    print("Enter the Number : ")
    iNo = int(input())

    print("Enter the position : ")
    iValue = int(input())

    iRet = OffBit(iNo, iValue)
    print("The updated value is : ", iRet)

if __name__ == "__main__":
    main()