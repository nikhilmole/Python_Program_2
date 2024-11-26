def StrCapCpy(str, dest):
    Start = 0
    End = len(str)
    strArr = list(str)

    while Start < End:
        if 'A' <= strArr[Start] <= 'Z':  
            dest.append(strArr[Start])
        
        Start += 1

    
    return ''.join(dest)

def main():
    print("Enter the String: ")
    Arr = input()

    Brr = []

    result = StrCapCpy(Arr, Brr)

    print("Uppercase letters:", result)

if __name__ == "__main__":
    main()
