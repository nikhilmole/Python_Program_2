iRev = 0
def Rev(iNo):

    global iRev

    iDigit = 0

    if(iNo > 0):
        iDigit = iNo % 10
        iRev = iRev * 10 + iDigit
        iNo = iNo // 10
    
        Rev(iNo)

    return iRev

def main():

    print("Enter the Number : ")
    iNo = int(input())

    iRet = Rev(iNo)

    print(iRet)

if __name__ == "__main__":
    main()