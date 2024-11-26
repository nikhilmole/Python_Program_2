def ChkDigit(ch):
    bFlag = False

    if (ch >= '0' and ch <= '9'):
        bFlag = True

    return bFlag

def main():

    print("Enher the character")
    cValue = input()

    bRet = ChkDigit(cValue)
    if(bRet == True):
        print("True")
    
    else:
        print("False")

if __name__ == "__main__":
    main()