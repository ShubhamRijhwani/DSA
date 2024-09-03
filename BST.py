class Node:
    def __init__(self,data=None,left=None,right = None):
        self.data = data
        self.lef = left
        self.right = right
class BST:
    def __init__(self):
        self.root = None
    
    def Insert(self,data):
        self.root = self.rInsert(self.root,data)
    def rInsert(self,root,data):
        if root is None:
            return Node(data)
        if data<root.data:
            root.left = self.rInsert(root.left,data)
        elif data>root.data:
            root.right = self.rInsert(root.right,data)
        return root
    
    def Search(self,data):
        return self.rSearch(self.root,data)
    def rSearch(self,root,data):
        if root is None or root.data == data:
            return root
        if data<root.data:
            return self.rSearch(root.left,data)
        else:
            return self.rSearch(root.right,data)
        
    def Inorder(self):
        result = []
        self.rInorder(self.root,result)
        return result
    def rInorder(self,root,result):
        if root:
            self.rInorder(root.left,result)
            result.append(root.data)
            self.rInorder(root.right,result)

    def Preorder(self):
        result = []
        self.rPreorder(self.root,result)
        return result
    def rPreorder(self,root,result):
        if root:
            result.append(root.data)
            self.rPreorder(root.left,result)
            self.rPreorder(root.right,result)     

    def Postorder(self):
        result = []
        self.rPostorder(self.root,result)
        return result
    def rPostorder(self,root,result):
        if root:
            self.rPostorder(root.left,result)
            self.rPostorder(root.right,result)
            result.append(root.data)

    def MinVal(self,temp):
        current = temp
        while current.left:
            current = current.left
        return current.data
    
    def MaxValue(self,temp):
        current = temp
        while current.right:
            current = current.right
        return current.data
    
    def delete(self,data):
        self.root = self.rDelete(self.root,data)
    def rDelete(self,root,data):
        if root is None:
            return root
        if data < root.data:
            root.left = self.rDelete(root.left, data)
        elif data > root.data:
            root.right = self.rDelete(root.right, data)
        else:
            if root.left is None:
                return root.right
            elif root.right is None:
                return root.left
            root.data = self.MinVal(root.right)
            self.rDelete(root.right,root.data)
        return root
    
    