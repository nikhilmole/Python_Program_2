def DisplayDigit(str):

    Start = 0
    End = len(str)
    ArrArray = list(str)

    while(Start < End):

        if(ArrArray[Start] >= '0')and(ArrArray[Start] <= '9'):

            print(ArrArray[Start])
    
        Start += 1

def main():

    print("Enter the string : ")
    Arr = input()

    DisplayDigit(Arr)

if __name__ == "__main__":
    main()