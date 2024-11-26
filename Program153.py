def Display(str):

    End = len(str)
    i = 0

    while(i < End):

        j = 0

        while(j < End):

            if(i >= j):

                print(str[j],end = '\t')

            else:

                print(end = '\t')

            j += 1
        
        print()
        
        i += 1

def main():

    print("Enter the String : ")
    Arr= input()

    Display(Arr)

if __name__ == "__main__":
    main()