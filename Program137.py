def StrCpyRev(str,dest):

    StrLength = len(str)-1

    while(StrLength >= 0):
        
        dest.append(str[StrLength])
        StrLength -= 1        

    return ''.join(dest)

def main():

    print("Enter the String : ")
    Arr = input()

    Brr = []

    result = StrCpyRev(Arr, Brr)

    print(result)

if __name__ == "__main__":
    main()