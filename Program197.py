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
            return
        
        while(temp != None):
            print(f"|{temp.data}|->",end = '')
            temp = temp.next

        print("null")

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

    def Maxi(self):
        iMax = 0
        iMin = 0
        temp = self.First
        while(temp != None):
            iMin = temp.data
            if(iMax < iMin):
                iMax = iMin
            
            temp = temp.next
    
        return iMax
    
def main():

    obj = SinglyLL()

    obj.InsertFirst(11)
    obj. InsertFirst(101)
    obj.InsertFirst(201)
    obj.InsertFirst(111)
    obj.InsertFirst(51)

    obj.Display()
    iRet = obj.Count()
    print("The node couont is :",iRet)

    iRet = obj.Maxi()
    print("The maximum number is : ",iRet)

if __name__ == "__main__":
    main()