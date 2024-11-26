iMax = 0
def Max(iNo):

    global iMax

    if(iNo > 0):

        iDigit = iNo % 10

        if(iDigit > iMax):
            iMax = iDigit
        
        iNo = iNo / 10

        Max(iNo)
        
    return iMax

def main():

    print("Enter the Number : ")
    iNum = int(input())

    iRet = Max(iNum)
    print("Maximum number is : ",iRet)

if __name__ == "__main__":
    main()