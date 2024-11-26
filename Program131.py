def Rev(str):

    Start = 0
    End = len(str)-1
    strlist = list(str)
    temp = '\0'

    while(Start < End):

        temp = strlist[End]
        strlist[End] = strlist[Start]
        strlist[Start] = temp

        Start += 1
        End -= 1

    Updated = ''.join(strlist)

    return Updated

def main():

    print("Enter the String")
    Arr = input()

    iRet = Rev(Arr)
    print(iRet)
if __name__ == "__main__":
    main()