def Display(ch):

    if((ch >= 'A')and(ch <= 'Z')):
        for i in range(ord(ch),ord('Z'),1):
            print(chr(i))
    
    elif((ch >= 'a')and(ch <= 'z')):
        for i in range(ord(ch),ord('z'),1):
            print(chr(i))

    else:
        print("Invalid option")
        
def main():

    print("Enter the character : ")
    cValue = input()

    Display(cValue)

if __name__ == "__main__":
    main()