def ChkFreq(str, ch):

    Start = 0
    End = len(str)
    CharArr = list(str)
    iCount = 0

    while(Start < End):

        if(CharArr[Start] == ch):

            iCount += 1

        Start += 1

    return iCount

def main():

    print("Enter the String  :")
    Arr = input()

    print("Enter the character : ")
    ch = input()

    iRet = ChkFreq(Arr, ch)

    print("the freq is : ",iRet)

if __name__ == "__main__":
    main()