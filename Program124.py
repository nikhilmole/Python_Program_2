def Toggle(str):

    Start = 0
    End = len(str)
    strlist = list(str)

    while(Start < End):
    
        if((strlist[Start] >= 'A')and(strlist[Start] <= 'Z')):
            
            strlist[Start] = chr(ord(strlist[Start]) + 32)
    
        elif((strlist[Start] >= 'a')and(strlist[Start] <= 'z')):

            strlist[Start] = chr(ord(strlist[Start]) - 32)

        Start += 1

        joinstr = ''.join(strlist)

        return joinstr

def main():

    print("Enter the string : ")
    Arr = input()   

    cRet = Toggle(Arr)

    print(cRet)

if __name__ == "__main__":
    main()