def ChkBit(iNum):

    iResult = 0
    iMask = 16400

    iResult = iNum & iMask

    if(iResult == iMask):
        return True
    
    return False

def main():

    print("Enter the Number : ")
    iNo = int(input())

    bRet = ChkBit(iNo)

    if(bRet == True):
        print("15 and 5 bit is on")
    else:
        print("15 and 5 bit is off")

if __name__ == "__main__":
    main()