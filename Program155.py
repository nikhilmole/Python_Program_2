def Display(str):

    strArr = list(str)
    End = len(str)

    for i in range(End):

        for j in range(End):

            if((strArr[j] >= 'A')and(strArr[j] <= 'Z')):

                strArr[j] = (chr)(ord(strArr[j]) + 32)

            print(strArr[j],end = '\t')

        print()

def main():
    
    print("Enter the String : ")
    Arr = input()

    Display(Arr)

if __name__ == "__main__":
    main()
 