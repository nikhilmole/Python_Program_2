def MaximumWordCount(str):

    CurrentCount = 0
    MaxCount = 0
    strArr = list(str)
    Start = 0
    End = len(str)

    while(Start < End):

        if(str[Start] == ' ' or Start == End):

            if(CurrentCount > MaxCount):

                MaxCount = CurrentCount

            CurrentCount = 0

        else:
            
            CurrentCount += 1

        Start += 1

    if(CurrentCount > MaxCount):

        MaxCount = CurrentCount

    return MaxCount

def main():

    print("Enter the String : ")
    Arr = input()

    iRet = MaximumWordCount(Arr)
    print(iRet)

if __name__ == "__main__":
    main()
    