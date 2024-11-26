def Palindrom(str):

    Start = 0
    End = len(str)-1
    strArr = list(str)

    while(Start < End):

        if(strArr[Start] >= 'A' and strArr[Start] <= 'Z'):
            strArr[Start] = chr(ord(strArr[Start]) + 32)

        if(strArr[End] >= 'A' and strArr[End] <= 'Z'):
            strArr[End] = chr(ord(strArr[End]) + 32)

        if(strArr[Start] != strArr[End]):

            return False
        
        Start += 1
        End -= 1

    return True

def main():

    print("Enter the String : ")
    Arr = input()

    bRet = Palindrom(Arr)
    if(bRet == True):
    
        print("Palindrome")
    
    else:
        print("non Palindrome")

if __name__ == "__main__":
    main()