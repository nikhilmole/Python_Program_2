def CountSmall(str):

    iCount = 0
    Index = 0
    Length = len(str)

    while(Index < Length):
        if(str[Index] >= 'a')and(str[Index] <= 'z'):
            iCount = iCount + 1

        Index = Index + 1
    
    return iCount

def main():

    print("Enter the string : ")
    Arr = input()

    iRet = CountSmall(Arr)
    
    print("The smal character are : ",iRet)

if __name__ == "__main__":
    main()