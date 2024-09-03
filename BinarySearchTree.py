#In BST recursion is used

class BinarySearchTree:
    def __init__(self,data):
        self.data =data
        self.left = None
        self.right = None

    def AddChild(self,data):
        if data == self.data: #Because BST cannot have duplicate items
            return
        
        if data<self.data: #add data in left subtree
            if self.left: #TO check if left element already have a value         
                self.left.AddChild(data) #if there is a value in left so we will simply use recursive function that will follow same steps
            else: #if there is no value in left just create a node
                self.left = BinarySearchTree(data)
        else: #For right sub tree
            if self.right:
                self.right.AddChild(data)
            else:
                self.right = BinarySearchTree(data)

    def InOrderTraaversal(self): #Left Root Right
        elements = [] #A empty list to return the values of tree in in order traversal method
        if self.left:
            elements += self.left.InOrderTraaversal() #Recursion
        
        elements.append(self.data) #for root node

        if self.right:
            elements += self.right.InOrderTraaversal()

        return elements  

    def search(self,val):
        if self.data==val:
            return True

        if val < self.data: #If value is smaller than data that it might be in left so will start checking for it from left
            if self.left:  #To check whether there are any values in left 
                return self.left.search(val)
            else:
                return False
        if val > self.data:
            if self.right:
                return self.right.search()
            else:
                return False

    def FindMin(self): #The mininmum value in tree will be most left node so we just need to reach there by recursively using same function till self.left value is none i.e. no value is present in left
        if self.left is None:
            return self.data
        return self.left.FindMin()

    def FindMax(self):
        if self.right is None:
            return self.data 
        return self.right.FindMax()

    def CalculateSum(self): #For calculating sum we will take sum left sum + data + right sum
        LeftSum = self.left.CalculateSum() if self.left else 0
        RightSum = self.right.CalculateSum() if self.right else 0
        return LeftSum + self.data + RightSum   

    def PreOrderTraversal(self): #Root Left Right
        elements = [self.data]  
        if self.left:
            elements += self.left.PreOrderTraversal()
       
        if self.right:
            elements += self.right.PreOrderTraversal() 

        return elements

    def PostOrderTraversal(self): #Left Right Root
        elements = []  
        if self.left:
            elements += self.left.PostOrderTraversal()
       
        if self.right:
            elements += self.right.PostOrderTraversal()

        elements.append(self.data)     

        return elements    

    def delete(self,val):
        if val<self.data:
            if self.left:
                self.left.delete(val)
        elif val>self.data:
            if self.right:
                self.right.delete(val)
        else:
            if self.left is None and self.right is None:
                return None
            if self.left is None:
                return self.right
            if self.right is None:
                return self.left

            #This method of delete is dony by using min value
            MinVal = self.right.FindMin() #Here we find min value from right
            self.data = MinVal
            self.right = self.right.delete(MinVal)
        return self

        
    # def MaximumDepth(self):
    #     d = 0
    #     if self.right or self.left:
    #         d+=1
    #     self.left = self.left.MaximumDepth()
    #     self.right = self.right.MaximumDepth()
    #     return d

            

def BuildTree(elements):
    root  = BinarySearchTree(elements[0]) #root will be the first element of list
    
    for i in range(1,len(elements)): #traversing in list to put it after root node
        root.AddChild(elements[i]) 

    return root




if __name__ == '__main__':
    numbers = [17,4,1,20,9,23,18,34]
    NumTree = BuildTree(numbers)
    NumTree.delete(20)
    print(NumTree.PreOrderTraversal())
    # print("Maximum depth :",NumTree.MaximumDepth())

