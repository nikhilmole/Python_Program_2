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

        while(temp != None):
            print(f"|{temp.data}|->",end='')
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
    
    def Addition(self):
        iAdd = 0

        temp = self.First

        while(temp != None):

            iAdd = iAdd + temp.data
            temp = temp.next

        return iAdd

def main():


    obj = SinglyLL()

    iRet = 0

    obj.InsertFirst(5)
    obj.InsertFirst(4)
    obj.InsertFirst(3)
    obj.InsertFirst(2)
    obj.InsertFirst(1)

    obj.Display()
    iRet = obj.Count()
    print("The node count is : ",iRet)

    iRet = obj.Addition()
    print("The node Addition is : ",iRet)
    
if __name__ == "__main__":
    main()