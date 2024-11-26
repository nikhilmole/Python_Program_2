def ChkVowels(str):

    Index = 0
    Length = len(str)
    bFlag = False
    while(Index < Length):
        if((str[Index] == 'A')or(str[Index] == 'E')or(str[Index] == 'I')or(str[Index] == 'O')or(str[Index] == 'U')or
            (str[Index] == 'a')or(str[Index] == 'e')or(str[Index] == 'i')or(str[Index] == 'o')or(str[Index] == 'u')):
            bFlag = True

        Index += 1
        
    return bFlag

def main():

    bRet = False

    print("Enter the String : ")
    Arr = input()

    bRet = ChkVowels(Arr)
    if(bRet == True):
        print("Vowel present")
    
    else:
        print("Vowel not present")
if __name__ == "__main__":
    main()