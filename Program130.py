def FirstOcc(str, ch):

    Start = 0
    End = len(str)
    strlist = list(str)
    iPose = -1
    iFreq = 1

    while(Start < End):
    
        if(strlist[Start] == ch):

            iPose = iFreq
        
        Start += 1
        iFreq += 1
    
    return iPose

def main():

    print("Enter the String : ")
    Arr = input()

    print("Enter the Character : ")
    ch = input()

    iRet = FirstOcc(Arr,ch)
    print("The first occ is : ",iRet)

if __name__ == "__main__":
    main()