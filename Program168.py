i = 1
ifacto = 1

def Facto(iNo):
    global i
    global ifacto

    if(i <= iNo):
        ifacto = ifacto * i
        i += 1
        Facto(iNo)

    return ifacto

def main():

    print("Enter the Number : ")
    iValue = int(input())

    iRet = Facto(iValue)
    print("the Factorials are : ",iRet)

if __name__ == "__main__":
    main()