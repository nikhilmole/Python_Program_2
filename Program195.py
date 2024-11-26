class node:
    def __init__(self,iNo):
        self.next = None
        self.data = iNo

class SinglyLL:
    def __init__(self):
        self.First = None
        self.iCnt = 0

    def Display(self):
        temp = None
        temp = self.First

        if(self.First == None):
            print("LL is empty")
            return
        
        while(temp != None):
            print(f"|{temp.data}|->",end = '')
            temp = temp.next
        
        print("None")

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

    def SearchLastOcc(self,iNo):

        temp = self.First   
        iCnt = 1
        iPos = -1

        while(temp != None):
            if(temp.data == iNo):

                iPos = iCnt

            iCnt += 1
            temp = temp.next

        return iPos    

def main():
    
    obj = SinglyLL()

    iRet = 0

    obj.InsertFirst(70)
    obj.InsertFirst(30)
    obj.InsertFirst(50)
    obj.InsertFirst(40)
    obj.InsertFirst(30)
    obj.InsertFirst(20)
    obj.InsertFirst(10)
    
    obj.Display()
    iRet = obj.Count()
    print("The Node count is : ",iRet)

    iRet = obj.SearchLastOcc(30)
    print("First occurance is : ",iRet)

if __name__ == "__main__":
    main()