class node:
    def __init__(self , data):
        self.data = data
        self.left = None
        self.right=None

    def printnode(self):
        print(self.data)
    def insert(self , val):
        if val< self.data:
            if self.left==None:
                self.left = node(val)
            else:
                self.left.insert(val)
        if val>= self.data:
            if self.right==None:
                self.right=node(val)
            else:
                self.right.insert(val)

    def printtree(self):
        if self.left !=None:
            self.left.printtree()
        print(self.data)
        if self.right !=None:
            self.right.printtree()

    def findval(self , val):
        if val>self.data:
            if self.right==None:
                return ("not found")
            return self.right.findval(val)
        if val<self.data:
            
            if self.left==None:
                return("not found")
            else:
                return self.left.findval(val)
        else:
            return "found"



temp = node(23)
temp.printnode()
temp.insert(2)
temp.insert(6)
temp.insert(9)
temp.insert(1)
temp.insert(12)
temp.insert(3)
temp.insert(15)
temp.insert(8)

temp.printtree()
temp.findval(34)
