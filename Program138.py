def WhiteSpaceRemoval(str, dest):

    Start = 0
    End = len(str)
    strArr = list(str)

    while(Start < End):

        if(strArr[Start] != ' '):

            dest.append(strArr[Start])

        Start += 1

    return ''.join(dest)

def main():

    print("Enter the string : ")
    Arr = input()

    Brr = []

    Result = WhiteSpaceRemoval(Arr,Brr)

    print(Result)

if __name__ == "__main__":
    main()