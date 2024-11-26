class N:
    def __init__(self,iSize):
        self.iLength = iSize
        self.Arr = []

    def Accept(self):
        print("Enter the numbers : ")
        for i in range(self.iLength):
            iNo = int(input())
            self.Arr.append(iNo)

    def Digits(self):
        print("The 3 digits numbers is : ")
        for i in range(self.iLength):
            if(self.Arr[i] > 99)and(self.Arr[i] < 1000):
                print(self.Arr[i]) 
def main():

    print("How many numbers you watn to add in array : ")
    iSize = int(input())

    nobj = N(iSize)

    nobj.Accept()
    nobj.Digits()

if __name__ == "__main__":
    main()