def ToggleBit(iNum, iStart, iEnd):

    i = 0
    iResult = 0
    iMask = 0

    for i in range(iStart, iEnd):

        iMask |= 1 << (i - 1)
    
    iResult = iMask ^ iNum

    return iResult 

def main():

    print("Enter the Number : ")
    iNo = int(input())

    print("Enter the Starting popsition : ")
    iValue1 = int(input())

    print("Enter the Endig popsition : ")
    iValue2 = int(input())

    iRet = ToggleBit(iNo, iValue1, iValue2)

    print(iRet)

if __name__ == "__main__":
    main()