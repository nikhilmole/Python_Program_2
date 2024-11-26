def Display(s):

    end = len(s)

    uppercase_str = ''

    for char in s:

        if 'a' <= char <= 'z':
            uppercase_str += chr(ord(char) - 32)

        else:
            uppercase_str += char  

    characters = uppercase_str.split()

    for i in range(end):
        for char in characters:
            print(char, end='\t')
        print()  

def main():
    Arr = input("Enter the String: ")

    Display(Arr)

if __name__ == "__main__":
    main()
