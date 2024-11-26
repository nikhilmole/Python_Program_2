def StrCnt(str, dest, iNo):
    Start = 0
    End = len(dest)
    strArr = list(str)  
    destArr = list(dest) 

    
    while Start < End and 0 < iNo:
        strArr.append(destArr[Start])
        Start += 1
        iNo -= 1

    return ''.join(strArr)  

def main():
    print("Enter the First String : ")
    Arr = input().strip()  

    print("Enter the second string : ")
    Brr = input().strip()  

    print("Enter the number : ")
    iNo = int(input().strip()) 

    result = StrCnt(Arr, Brr, iNo)
    print(result)

if __name__ == "__main__":
    main()
