def StrUpperToLower(str):

    Start = 0
    End = len(str) - 1
    Array = list(str)

    while(Start <= End):
        if((Array[Start] >= 'A')and(Array[Start] <= 'Z')):

            Array[Start]= chr(ord(Array[Start]) + 32)

        Start += 1

    Result =  ''.join(Array)

    return Result

def main():

    print("Enter the String")
    Arr = input()

    bRet = StrUpperToLower(Arr)
    print(bRet)
if __name__ == "__main__":
    main()