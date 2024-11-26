iPro = 1
def Pro(iNo):
    
    global iPro

    iDigit = 0

    if(iNo > 0):

        iDigit = iNo % 10
        iPro = iPro * iDigit
        iNo = iNo // 10
        Pro(iNo)

    return iPro

def main():

    print("Enter the Number : ")
    iNo = int(input())

    iRet = Pro(iNo)

    print("The product is : ",iRet)

if __name__ == "__main__":
    main()