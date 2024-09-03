class Stack:
    def __init__(self):
        self.items=[]
    def is_empty(self):
        return len(self.items) == 0
    def push(self,data):
        self.items.append(data)
    def pop(self,data):
        if not self.is_empty():
            return self.items.pop()
        else:
            return print("Stack is Empty")
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        else:
            return print("Stack is empty")
    def size(self):
        return len(self.items)
    
s1 = Stack()
s1.push(10)
s1.push(20)
s1.push(30)
print(s1.peek())