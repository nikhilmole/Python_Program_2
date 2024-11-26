i = 1

def Display(iNum, ch):
    global i

    if(iNum < 0):

        iNum = -iNum

    if(i <= iNum)and(ch != ' '):

        print(ch,end = '\t')

        ch = chr(ord(ch) + 1)

        i+=1

        Display(iNum, ch)

def main():
    
    print("Enter the Character : ")
    ch = input()

    print("Enter the Number : ")
    iNo = int(input())

    Display(iNo,ch)

if __name__ == "__main__":
    main()
