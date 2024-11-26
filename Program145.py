def RevStringWithToggle(str):

    Start = 0
    End = len(str)-1
    temp = '\0'
    strArr = list(str)

    while(Start < End):

        if(strArr[Start] >= 'A' and strArr[Start] <= 'Z'):
            strArr[Start] = chr(ord(strArr[Start]) + 32)

        elif(strArr[Start] >= 'a' and strArr[Start] <= 'z'):
            strArr[Start] = chr(ord(strArr[Start]) - 32)

        if(strArr[End] >= 'A' and strArr[End] <= 'Z'):
            strArr[End] = chr(ord(strArr[End]) + 32)

        elif(strArr[End] >= 'a' and strArr[End] <= 'z'):
            strArr[End] = chr(ord(strArr[End]) - 32)

        temp = strArr[End]
        strArr[End] = strArr[Start]
        strArr[Start] = temp

        Start += 1
        End -= 1

    return ''.join(strArr)

def main():

    print("Enter the String : ")
    Arr = input()

    result = RevStringWithToggle(Arr)

    print(result)

if __name__ == "__main__":
    main()