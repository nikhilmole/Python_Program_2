def ChkAlpha(ch):
    bFlag = False

    if((ch >= 'A')and(ch <= 'Z'))or((ch >= 'a')and(ch >= 'z')):
        bFlag = True
        
    return bFlag

def main():
    print("Enter Character : ")
    cValue = input()

    bRet = ChkAlpha(cValue)
    if(bRet == True):
        print("True")
    
    else:
        print("False")

if __name__ == "__main__":
    main()