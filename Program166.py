iSum = 0
def DigiSum(iNo):

    global iSum

    if(iNo > 0):

        iDigit = iNo % 10
        iSum = iSum + iDigit
        iNo = iNo // 10
        DigiSum(iNo)
        
    return iSum

def main():

    print("Enter the Number : ")
    iValue = int(input())

    iRet = DigiSum(iValue)
    print(iRet)

if __name__ == "__main__":
    main()