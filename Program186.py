def CommonBit(iNum1, iNum2):

    CommonBit = iNum1 & iNum2
    Position = 0

    while(CommonBit):

        if(CommonBit & 1):

            print("CommonBit Are : ",Position,end = '\t')
        
        CommonBit >>= 1
        Position += 1

def main():

    print("Enter the First number : ")
    iNo1 = int(input())

    print("Enter the First number : ")
    iNo2 = int(input())

    CommonBit(iNo1, iNo2)

if __name__ == "__main__":
    main()