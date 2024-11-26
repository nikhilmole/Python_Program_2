def OffBit(iNum):

    iResult = 0
    iMask = 0xFFFFFDBF

    iResult = iMask & iNum

    return iResult

def main():

    print("Enter the Number : ")
    iNo = int(input())

    iRet = OffBit(iNo)
    print("The updated number is : ")

if __name__ == "__main__":
    main()