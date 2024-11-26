def StrCpy(str,dest,iCnt):

    Start = 0
    End = len(str)
    StrArr = list(str)

    while(Start < End) and (iCnt > 0):

        dest.append(StrArr[Start])
        Start += 1
        iCnt -= 1

    return ''.join(dest)


def main():

    print("Enter the String : ")
    Arr = input()

    Brr = []

    print("Enter number : ")
    iNo = int(input())

    result = StrCpy(Arr,Brr,iNo)

    print("Compy string is : ",result)

if __name__ == "__main__":
    main()