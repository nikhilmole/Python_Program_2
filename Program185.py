def CountOnBits(iNum):

    iCnt = 0

    while(iNum > 0):

        iCnt = iCnt + (iNum & 1)

        iNum >>= 1

    return iCnt
def main():

    print("Enter the number : ")
    iNo = int(input())

    iRet = CountOnBits(iNo)
    print("On bits are : ",iRet)

if __name__ == "__main__":
    main()