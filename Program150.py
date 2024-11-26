def Display(str):

    Start = 0
    End = len(str)-1

    while(str[Start] != str[End]):

        j = 0

        while(str[j] != str[End]):

            print(str[j], end = '\t')
            
            j += 1

        Start += 1
        print()

def main():

    print("Enter the String : ")
    Arr = input()   

    Display(Arr)
    
if __name__ == "__main__":
    main()