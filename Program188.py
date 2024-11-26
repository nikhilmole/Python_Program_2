def ChkBit(iNum, iPos1, iPos2):

    iMask1 = 1 << (iPos1 - 1)
    iMask2 = 1 << (iPos2 - 1)

    iResult1 = iNum & iMask1
    iResult2 = iNum & iMask2

    if(iMask1 == iResult1)and(iMask2 == iResult2):
        return True
    
    return False

def main():

    bRet = False

    print("Enter the number : ")
    iNo = int(input())

    print("Enter the 1st positon : ")
    iNum1 = int(input())

    print("Enter the second position : ")
    iNum2 = int(input())

    bRet = ChkBit(iNo, iNum1, iNum2)

    if(bRet == True):
        print("True")
    
    else:
        print("False")

if __name__ == "__main__":
    main()