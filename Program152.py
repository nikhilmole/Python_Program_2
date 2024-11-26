def Display(str):

    End = len(str)

    for i in range(End):

        for j in range(End):

            if(j < End - i):

                print(str[j], end = '\t')

            else:

                print(end = '\t')

        print()

def main():

    print("Enter the String : ")
    Arr = input()

    Display(Arr)

if __name__ == "__main__":
    main()