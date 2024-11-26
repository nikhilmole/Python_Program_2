def ChkBit(iNum):

    iResult = 0
    iMask = 2147483649

    iResult = iMask & iNum

    if(iResult == iMask):
        return True

    return False

def main():

    print("Enter the number : ")
    iNo = int(input())
    bRet = False

    bRet = ChkBit(iNo)
    if(bRet == True):
        print("on")
    else:
        print("Off")

if __name__ == "__main__":
    main()