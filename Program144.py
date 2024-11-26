def StrCmpX(str, dest, iNo):

    Start = 0

    while((Start < len(str))and(Start < len(dest)) and(iNo > 0)):

        if(str[Start] != dest[Start]):
            return False
        
        Start += 1
        iNo -= 1
    
    if(iNo == 0):

        return True
    
    else:
        return False


def main():

    print("Enter the String : ")
    Arr = input()

    print("Enter the Second String : ")
    Brr = input()

    print("Enter the number : ")
    iNo = int(input())

    bRet = StrCmpX(Arr, Brr, iNo)
    if(bRet == True):
        print("Both String are same")

    else:
        print("Strings are not same")

if __name__ == "__main__":
    main()