def Convert(ch):

    if((ch >= 'A')and(ch <= 'Z')):
        print(chr(ord(ch) + 32))

    elif((ch >= 'a')and(ch <= 'z')):
        print(chr(ord(ch) - 32))
        
    else:
        print(ch)

def main():

    print("Enter the character : ")
    cValue = input()

    Convert(cValue)

if __name__ == "__main__":
    main()