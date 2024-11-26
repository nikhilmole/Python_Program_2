def Reverse(str):

    temp = '\0'
    Start = 0
    End = len(str) - 1
    Rev = list(str)

    while(Start < End):
        temp = Rev[End]
        Rev[End] = Rev[Start]
        Rev[Start] = temp

        Start += 1
        End -= 1

    return ''.join(Rev) 

def main():

    print("Enter the string : ")
    Arr = input()

    iRet = Reverse(Arr)

    print("The reveres string is : ",iRet)

if __name__ == "__main__":
    main()