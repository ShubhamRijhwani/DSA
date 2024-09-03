#The pointer in stack starts from top of stack !! Not from the bottom i.e. self.head isatt top

class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class Stack:
    def __init__(self):
        self.head = None

    def IsEmpty(self):
        if self.head==None:
            return True
        else:
            return False

    def Push(self,data):
        if self.head == None:
            self.head = Node(data)
        else:
            newnode =Node(data) #Here a new node is made with only data
            newnode.next = self.head #here self.head is assigned to newnode's next(address)
            self.head = newnode #here anoter new node is linked to self.head

    def Pop(self):
        if self.IsEmpty():
            return None
        else:
            PoppedNode = self.head #Now self.head is assigned to Popped Node
            self.head = self.head.next 
            PoppedNode.next = None
            return PoppedNode.data 

    def display(self):
        itr = self.head
        if self.IsEmpty():
            print("Stack Underflow")
        else:
            while itr != None:
                print(itr.data,end="")
                itr= itr.next 
                if(itr!=None):
                    print("-->",end="")
            return        

    def peek(self): #This function shows top of the data                      
        if self.IsEmpty():
            return None
        else:
            print(self.head.data)


if __name__ == '__main__':
    sk = Stack()
    sk.Push(5)
    sk.Push(6)
    sk.Push(8)
    sk.peek()
    sk.display()