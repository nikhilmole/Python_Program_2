def Toggle(iNum):

    iResult = 0
    iMask = 0x00000240

    iResult = iMask ^ iNum

    return iResult

def main():


    print("Enter the number : ")
    iNo = int(input())

    iRet = Toggle(iNo)

    print("The updated number is",iRet)

if __name__ == "__main__":
    main()