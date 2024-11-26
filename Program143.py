def StrCmpX(str, dest):

    Start = 0

    while(Start < len(str) and (Start < len(dest))):
        if(str[Start]) != (dest[Start]):

            return False
        
        Start += 1

    if(Start == len(str))and(Start == len(dest)):

        return True
    
    else:

        return False

def main():

    print("Enter the Fist string : ")
    Arr = input()

    print("Enter the Second String : ")
    Brr = input()

    bRet = StrCmpX(Arr,Brr)
    if(bRet == True):
        print("Strings Are same")

    else:
        print("String are not same")

if __name__ == "__main__":
    main()