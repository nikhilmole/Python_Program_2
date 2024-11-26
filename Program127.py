def ChkChar(str, ch):

    bFlag = False
    Start = 0
    End = len(str)  
    strlist = list(str)

    while(Start < End):

        if(strlist[Start] == ch):

            bFlag = True

        Start += 1

    return bFlag

def main():

    print("Enter the string : ")
    Arr = input()

    print("Enter the character : ")
    let = input()

    bRet = False

    bRet = ChkChar(Arr,let)

    if(bRet == True):
        print("The character is presnet")

    else:
        print("The character is not present")

if __name__ == "__main__":
    main()