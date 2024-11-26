def StrCpy(str,dest):

    Start = 0
    End = len(str)
    strArr = list(str)

    while(Start < End):

        if((str[Start] >= 'a')and(str[Start] <= 'z')):

            dest.append(str[Start])

        Start += 1

    return ''.join(dest)

def main():

    print("Enter the String : ")
    Arr = input()

    Brr = []

    result = StrCpy(Arr, Brr)

    print("Small let are : ",result)

if __name__ == "__main__":
    main()