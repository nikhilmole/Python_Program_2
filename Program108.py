def ChkAlphaCapi(ch):

    bFlag = False

    if((ch >= 'A')and(ch <= 'Z')):
        bFlag = True

    return bFlag

def main():
    bRet = False

    print("Enter the character : ")
    cValue = input()

    bRet = ChkAlphaCapi(cValue)

    if(bRet == True):
        print("True")
    
    else:
        print("False")

if __name__ == "__main__":
    main()