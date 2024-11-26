def StrCpy(str, dest):

    Start = 0
    End = len(str)

    while(Start < End):

        dest.append(str[Start])

        Start += 1
        
    return ''.join(dest)

def main():

    Arr = "Marvellous Multi Os"
    Brr = []

    iRet = StrCpy(Arr, Brr)

    print("The copy string is : ",iRet)

if __name__ == "__main__":
    main()