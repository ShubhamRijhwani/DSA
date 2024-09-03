#whenever we are using while loop we are just iterating through our list.

class Node:
    def __init__(self, data=None,next=None):
        self.data=data
        self.next=next

class Linkedlist:
    def __init__(self):
        self.head=None

    def is_empty(self):
        return self.head==None

    def InserAtBeginning(self,data):
        node = Node(data,self.head)#As this is beginning so we will create a node with self.head pointing the next value
        self.head=node

    def print(self):
        if self.head is None:
            print("Our linked list is empty")
            return

        #if linked list is not empty we will assign a variable to head value
        itr = self.head
        llstr = ''#empty linked list 
        while itr:
            llstr += str(itr.data) + '--->'
            itr = itr.next

        print(llstr) 

    def InsertAtEnd(self,data):
        if self.head is None:#if linked list is blank
            self.head = Node(data,None)
            return

        #if linked list is not empty we will iterate to the end and insert at end
        itr = self.head
        while itr.next: #By this while loop we are just iterating till the end and assigning itr.next to itr
            itr = itr.next

        #Now when itr.next is not null that means we reached at the end now we will print the itr.next value
        itr.next = Node(data,None)

    def InserValues(self,data_list):
        self.head=None#To delete all the data to make a new ll with a list as ll
        for data in data_list:
            self.InsertAtEnd(data)   
    
    def search(self,data):
        itr = self.head
        while itr.next:
            if itr.data == data:
                return itr
            itr = itr.next
        return None

    def length(self):
        count = 0
        itr = self.head
        while itr:
            count += 1
            itr = itr.next

        return count
    
    def RemoveFirst(self):
        if self.head:
            self.head = self.head.next
    
    def RemoveLast(self):
        if self.head is None:
            pass
        elif self.head.next is None:
            self.head = None
        else:
            itr = self.head
            while itr.next.next is not None:
                itr = itr.next
            itr.next = None
        

    def RemoveAt(self,index):
        if index<0 or index>self.length():
            raise Exception("Invalid Index")
        if index == 0:
            self.head = self.head.next   
            return

        count = 0
        itr = self.head
        while itr:
            if count == index-1:
                itr.next = itr.next.next
                break
            itr = itr.next
            count += 1

    def InsertAt(self,index,data):
        if index<0 or index>self.length():
            raise Exception("Invalid Index")     

        if index == 0:
            self.InserAtBeginning()
            return

        count = 0
        itr = self.head
        while itr:
            if count == index - 1:#beacuse we add linked list by giving its address to previous node's next
                node = Node(data,itr.next)
                itr.next = node
                break
            itr = itr.next       
            count += 1  

    def InsertAfterValues(self, data_after, data_to_insert):
        if self.head is None:
            return

        if self.head.data==data_after:
            self.head.next = Node(data_to_insert,self.head.next)
            return

        itr = self.head
        while itr:
            if itr.data == data_after:
                itr.next = Node(data_to_insert, itr.next)
                break

            itr = itr.next

    def RemoveByValue(self,data):
        if self.head is None:
            return

        if self.head.data ==  data:
            self.head = self.head.next
            return

        itr = self.head
        while itr.next:
            if itr.next.data == data:
                itr.next = itr.next.next
                break
            itr = itr.next   


    def __iter__(self):
        return SLLIterator(self.head)    

class SLLIterator: #To make our linked list iterable like string or list
    def __init__(self,start):
        self.current = start
    def __iter__(self):
        return self
    def __next__(self):
        if not self.current:
            raise StopIteration
        data = self.current.data
        self.current=self.current.next
        return data
    


if __name__ == '__main__':
    ll = Linkedlist()
    ll.InserValues([1,2,3,4,5])
    ll.RemoveAt(3)
    for i in ll:
        print(i)
    ll.print()