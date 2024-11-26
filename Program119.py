def Dif(str):

    iCountCapi = 0
    iCountSmall = 0
    Length = len(str)
    Index = 0

    while(Index < Length):
        if((str[Index] >= 'A')and(str[Index] <= 'Z')):
            iCountCapi += 1
        else:
            iCountSmall += 1
        Index += 1
    return iCountSmall - iCountCapi

def main():

    print("Enter the String : ")
    Arr = input()

    iRet = Dif(Arr)
    print("The dif is : ",iRet)

if __name__ == "__main__":
    main()