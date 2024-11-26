def StrLowerToUpper(str):

    Start = 0
    End = len(str)
    Name = list(str)

    while(Start < End):
        if((Name[Start] >= 'a')and(Name[Start] <='z')):
            Name[Start] = chr(ord(Name[Start]) - 32)

        Start += 1
    
    Rejoin = ''.join(Name)

    return Rejoin
def main():

    print("Enter the string : ")
    Arr = input()

    bRet = StrLowerToUpper(Arr)
    print(bRet)

if __name__ == "__main__":
    main()