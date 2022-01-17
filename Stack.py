class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
    def Display_Nodes(self):
        print("The node in stack is: ", self.data)
class Stack:
    def __init__(self):
        self.head = None
        self.size = 0
        
    def Push(self,node):
        if self.head == None:
            self.head = node
            self.size = self.size + 1
        else:
            node.next = self.head
            self.head = node
            self.size = self.size + 1
            
    def POP(self):
        if self.head == None:
            print("Your stack is empty")
            return
        else:
            temp = self.head
            self.head = self.head.next
            temp = None
            self.size = self.size - 1
    def PEEK(self):
        print("Element at the top of the stack is: ", self.head.data)
        
    def Is_Empty(self):
        if self.size == 0:
            print("your stack is empty")
        else:
            print("your stack is having some values")
            
    def Size(self):
        print("The size of your stack is: ", self.size)
        
    def Print_Stack(self):
        if self.head == None:
            print("Your stack is empty")
        Temp = self.head
        while Temp != None:
            Temp.Display_Nodes()
            Temp = Temp.next
OBJ = Stack()
OBJ.Push(Node(10))
OBJ.Push(Node(11))
OBJ.Push(Node(20))
OBJ.Push(Node(100))
OBJ.Push(Node(200))
OBJ.Print_Stack()
OBJ.POP()
OBJ.POP()
print("after Deletiom:")
OBJ.Print_Stack()
OBJ.PEEK()
OBJ.Is_Empty()
OBJ.Size()
OBJ.Push(Node(30))
OBJ.Push(Node(40))
print("After Adding Nodes")
OBJ.Print_Stack()