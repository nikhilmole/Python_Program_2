class node:
    def __init__(self,iNo):
        self.next = None
        self.data = iNo

class SinglyLL:
    def __init__(self):
        self.First = None
        self.iCnt = 0

    def Display(self):
        temp = self.First
        if(temp == None):
            print("The LL is empty")

        while(temp != None):
            print(f"|{temp.data}|->",end = '')
            temp = temp.next
        
        print("NULL")
    
    def Count(self):
        return self.iCnt

    def InsertFirst(self,iNo):
        newn = node(iNo)

        if(self.First == None):
            self.First = newn

        else:
            newn.next = self.First
            self.First = newn

        self.iCnt += 1

    def PerfectNum(self):
        temp = self.First
        i = 0
        iNum = 0

        while(temp != None):
            iNum = temp.data
            iSum = 0
            for i in range(1,iNum // 2 + 1):
                if(iNum % i == 0):
                    iSum = iSum + i
                
            if((iNum == iSum)and(iNum != 1)):
                print(f"{iNum} is a perfect number")
            
            temp = temp.next

def main():
    obj = SinglyLL() 

    obj.InsertFirst(89)
    obj.InsertFirst(6)
    obj.InsertFirst(41)
    obj.InsertFirst(17)
    obj.InsertFirst(28) 
    obj.InsertFirst(11)

    obj.Display()

    obj.PerfectNum()

if __name__ == "__main__":
    main()