def OnBit(iNum, iPos):

    iMask = 0
    iResult = 0

    iMask = 1 << (iPos - 1)

    iResult = iMask | iNum

    return iResult

def main():

    print("Enter the Number : ")
    iNo = int(input())

    print("Enter the Position : ")
    iValue = int(input())

    iRet = OnBit(iNo, iValue)

    print("The updated values is : ", iRet)

if __name__ == "__main__":
    main()