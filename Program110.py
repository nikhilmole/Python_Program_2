def ChkCapitalofSmall(ch):

    bFlag = False

    if(ch >= 'a')and(ch <= 'z'):
        bFlag = True

    return bFlag

def main():
    bRet = False

    print("Enter the character : ")
    cValue = input()

    bRet = ChkCapitalofSmall(cValue)

    if(bRet == True):
        print("Small character")
    
    else:
        print("Capital character")
if __name__ == "__main__":
    main()