def Toggle(iNum, iPos):

    iMask = 0
    iResult = 0

    iMask = 1 << (iPos - 1)

    iResult = iMask ^ iNum

    return iResult

def main():

    print("Enter the NUmber : ")
    iNo = int(input())

    print("Enter the Position : ")
    iValue = int(input())

    iRet = Toggle(iNo, iValue)
    print("The updated value is : ",iRet)

if __name__ == "__main__":
    main()