def ChkBit(iNum, iPos):

    iResult = 0
    iMask = 0

    iMask = 1 << (iPos -1)
    
    iResult = iMask & iNum

    if(iResult == iMask):
        return True

    return False

def main():

    print("Enter the Number : ")
    iNo = int(input())

    print("enter the position : ")
    iValue = int(input())

    bRet = ChkBit(iNo,iValue)

    if(bRet == True):
        print("ON")

    else:
        print("OFF")

if __name__ == "__main__":
    main()