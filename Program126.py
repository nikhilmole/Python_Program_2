def CountWhiteSpaces(str):

    Start = 0
    End = len(str)
    CharArr = list(str)
    iCount = 0
    
    while(Start < End):
    
        if(CharArr[Start] == ' '):
            
            iCount += 1
        
        Start += 1

    return iCount

def main():

    print("Enter the String : ")
    Arr = input()

    iRet = CountWhiteSpaces(Arr)

    print("Number of white spaces is : ",iRet)

if __name__ == "__main__":
    main()