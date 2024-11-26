def StrCnt(str, dest):

    str = str + dest

    return str

def main():

    print("Enter the String : ")
    Arr = input()

    print("Enter the second string : ")
    Brr = input()

    result = StrCnt(Arr, Brr)
    print(result)

if __name__ == "__main__":
    main()