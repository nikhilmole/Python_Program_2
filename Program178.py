def ChkBit(iNum):

    iResult = 0
    iMask = 488

    iResult = iMask & iNum

    if(iResult == iMask):
        return True

    return False

def main():

    print("Enter the number : ")
    iNo = int(input())

    bRet = ChkBit(iNo)
    if(bRet == True):
        print("The 7 8 9 bit is on")
    
    else:
        print("The 7 8 9 bit is off")

if __name__ == "__main__":
    main()