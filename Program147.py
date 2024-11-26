def WordCount(str):

    iCnt = 0
    Start = 0
    strArr = list(str)
    inword = False
    End = len(str)

    while(End == 0):
        return -1
    
    while(Start < End):
        
        if(strArr[Start] == ' '):
            
            inword = False

        elif(not inword):
            inword = True
            iCnt += 1

        Start += 1
    
    return iCnt

def main():

    print("Enter the string : ")
    Arr = input()

    iRet  = WordCount(Arr)
    print(iRet)

if __name__ == "__main__":
    main()