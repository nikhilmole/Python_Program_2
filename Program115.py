def ChkSymbol(ch):

    bFlag = False

    if((ch == '!')or(ch == '@')or(ch == '#')or(ch == '$')or(ch == '%')or(ch == '^')or(ch == '&')or(ch == '*')):
        bFlag = True
    
    return bFlag

def main():

    bRet = False

    print("Enter the character : ")
    cValue = input()

    bRet = ChkSymbol(cValue)

    if(bRet == True):
        print("Special symbol")
    else:
        print("not special symbol")

if __name__ == "__main__":
    main()