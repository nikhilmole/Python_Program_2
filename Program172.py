Start = 0
iCount = 0

def CountSmall(str):

    End = len(str)
    global iCount
    global Start

    if(Start < End):

        if(str[Start] >= 'a'and str[Start] <= 'z'):

            iCount += 1
        
        Start += 1
        CountSmall(str)

    return iCount


def main():

    print("Enter the String : ")
    Arr = input()

    iRet = CountSmall(Arr)
    print(iRet)

if __name__ == "__main__":
    main()