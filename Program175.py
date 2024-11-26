def ChkBit(iNum):

    iResult = 0
    iMask = 16384

    iResult = iNum & iMask


    if(iResult == iMask):
        return True
    
    return False

def main():

    print("Enter the Number : ")
    iNo = int(input())

    bRet = ChkBit(iNo)
    if(bRet == True):
        print("The 15th bit is on")
    else:
        print("The 15th bit is off")

if __name__ == "__main__":
    main()