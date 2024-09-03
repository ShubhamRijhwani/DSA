class Queue:
    def __init__(self):
        self.items=[]
        # self.front = None
        # self.rear = None
    def isEmpty(self):
        return len(self.items)==0
    def enqueue(self,data):
        self.items.append(data)
    def dequeue(self):
        if not self.isEmpty:
            self.items.pop(0)
        else:
            raise IndexError("Queue underflow")
    def getFront(self):
        if not self.isEmpty:
            return self.items[0]
        else:
            raise IndexError("Queue underflow")
    def getRear(self):
        if not self.isEmpty:
            return self.items[-1]
        else:
            raise IndexError("Queue underflow")
    def size(self):
        return len(self.items)