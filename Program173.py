iMin = 9
def Min(iNo):

    if(iNo == 0):
        print("You enter wrong number plss enter 1 to 9 values")
        return

    if(iNo < 0):
        iNo = -iNo

    global iMin 
    iDigit = 0

    if(iNo > 0):

        iDigit = iNo % 10
        if(iDigit < iMin):
            iMin = iDigit 
        iNo = iNo // 10

        Min(iNo)

    return iMin
def main():

    print("Enter the number : ")
    iNo = int(input())

    iRet = Min(iNo)
    print(iRet)

if __name__ == "__main__":
    main()