class Node:
    def __init__(self,data = None,prev=None,next=None):
        self.data = data
        self.prev = prev
        self.next = next

class DoubleLinkedList:
    def __init__(self):
        self.head = None

    def PrintForward(self):
        if self.head is None:
            print("Our linked list is empty")
            return

        itr = self.head
        dllstr = ''
        while itr:
            dllstr += str(itr.data) + '--->' 
            itr = itr.next
        print(dllstr)

    def GetLastNode(self):
        itr = self.head
        while itr.next:
            itr = itr.next
        return itr 

    def PrintBackword(self):
        if self.head is None:
            print("Our linked list is empty")
            return

        LastNode = self.GetLastNode()
        itr = LastNode
        dllstr = ''
        while itr:
            dllstr += str(itr.data) + '--->'
            itr = itr.prev
        print(dllstr)

    def InsertAtBeginning(self,data):
        if self.head == None:#If list is empty
            node = Node(data , None ,self.head)
            self.head = node
        else:#If there are elements in list 
            node = Node(data,None,self.head)
            self.head.prev = node#Here as there are elements present in linked list so we need to add nodes at both places next and previous
            self.head = node

    def InsertAtEnd(self,data):
        if self.head is None:
            self.head = Node(data,None,None)#Here we took 'self.head =' because we are insering at last that means there must be some elemnts in linked list or code will assume that there are some elemnets in dll     
            return

        itr = self.head
        while itr.next:#beacause we need to iterate till the end 
            itr = itr.next
        itr.next = Node(data,itr,None)

    def GetLength(self):
        count = 0
        itr = self.head
        while itr:
            count+=1
            itr = itr.next   
        return count

    def InserAt(self,index,data):
        if index<0 or index>self.GetLength():
            raise Exception("Invalid Index")     

        if index == 0:
            self.InserAtBeginning()
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                node = Node(data,itr,itr.next)
                if node.next:#This also means if node.next is not none
                    node.next.prev = node
                itr.next = node
                break
            itr =itr.next
            count +=1  

    def RemoveAt(self,index):
        if index<0 or index>self.GetLength():
            raise Exception("Invalid Index")

        if index == 0:
            self.head = self.head.next

        count = 0 
        itr = self.head
        while itr:
            if count == index:
                itr.prev.next = itr.next
                if itr.next:
                    itr.next.prev = itr.next
                break                
            itr = itr.next
            count+=1

    def InsertValues(self,data_list):
        self.head = None
        for data in data_list:
            self.InsertAtEnd(data)





if __name__ == '__main__':
    dll = DoubleLinkedList()
    dll.InsertValues([1,2,3,4,56])
    dll.PrintForward()