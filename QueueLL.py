#when self.rear pointer is pushed forward it is enqueue
#when self.front pointer is pushed forward it is dequeue

class Node:
    def __init__(self,data = None):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.front = self.rear = None #Both the pointers are at start of linked list(queue)

    def IsEmpty(self):
        return self.front == None    

    def enqueue(self,data):
        temp = Node(data) # first create a node then check for conditions and assign the pointers to the node
        if self.rear == None: #This condition is for when then there is no value in queue
            self.front = self.rear = temp
            return
        self.rear.next = temp # a node is created next to self.rear which is pointed by self.rear
        self.rear = temp #self.rear is itself is node just like self.head in stack

    def dequeue(self,data):
        if self.IsEmpty():
            return
        temp = self.front
        self.front = temp.next

        if self.front==None:
            self.rear==None

if __name__ == '__main__':
    q = Queue()
    q.enqueue(5)
    q.enqueue(6)
    q.enqueue(7)
    print("Queue Front : " + str(q.front.data if q.front != None else -1))
    print("Queue Rear : " + str(q.rear.data if q.rear != None else -1))            