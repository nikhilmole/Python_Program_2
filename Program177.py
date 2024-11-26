def ChkBit(iNum):

    iResult = 0
    iMask = 135282752

    iResult = iNum & iMask

    if(iResult == iMask):
        return True

    return False

def main():

    print("Enter the Number: ")
    iNo = int(input())

    bRet = ChkBit(iNo)
    if(bRet == True):
        print("5 15 21 & 25 Bit is on")

    else:
        print("5 15 21 & 25 Bit is off")

if __name__ == "__main__":
    main()