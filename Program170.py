iCount = 0
Start = 0

def CoutWhiteSpace(str):
    End = len(str)
    global iCount
    global Start

    if(Start < End):
        if(str[Start] == ' '):
            iCount += 1

        Start += 1
        CoutWhiteSpace(str)

    return iCount
def main():

    print("Enter the string : ")
    Arr = input()
    
    iRet = CoutWhiteSpace(Arr)
    print(iRet)

if __name__ == "__main__":
    main()