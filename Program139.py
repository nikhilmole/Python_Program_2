def StrCpyConvertCap(str, dest):

    Start = 0
    End = len(str)
    strArr = list(str)

    while(Start < End):

        if(strArr[Start] >= 'A')and(strArr[Start] <= 'Z'):

            dest.append(strArr[Start])

        elif(strArr[Start] >= 'a')and(strArr[Start] <= 'z'):

            dest.append(chr(ord(strArr[Start]) - 32))

        else:
            dest.append(strArr[Start])
        
        Start += 1

    return ''.join(dest)
    
def main():

    print("Enter the String : ")
    Arr = input()

    Brr = []

    result = StrCpyConvertCap(Arr, Brr)
    print(result)

if __name__ == "__main__":
    main()