def ChkFirstOcc(str, ch):

    Start = 0
    End = len(str)
    strList = list(str)
    iFreq = 1
    iPose = -1

    while(Start < End):

        if(strList[Start] == ch):

            iPose = iFreq
            break

        Start += 1
        iFreq += 1

    return iPose

def main():

    print("Enter the string : ")
    Arr = input()

    print("Enter the character : ")
    ch = input()

    iRet = ChkFirstOcc(Arr, ch)

    print("Enter the First oc is : ",iRet)

if __name__ == "__main__":
    main()