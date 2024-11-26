def OnorOff(iNum):

    iMask = 2304
    iRetult = 0

    iResult = iMask & iNum

    if(iMask == iResult):
        return True

    return False

def main():
    bRet = False

    print("Enter the Number :")
    iNo = int(input())

    bRet = OnorOff(iNo)
    if(bRet == True):
        print("The 9th 0or 12th bit is on")
    else:
        print("the 9th or 12th bit is off")

if __name__ == "__main__":
    main()