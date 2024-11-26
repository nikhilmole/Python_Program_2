def OnBit(iNum):

    iResult = 0
    iMask = 0x0F

    iResult = iMask | iNum

    return iResult

def main():

    print("Enter the nummber : ")
    iNo = int(input())

    iRet = OnBit(iNo)

    print("The updated number is : ",iRet)

if __name__ == "__main__":
    main()