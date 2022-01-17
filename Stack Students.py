class Node:    
    def __init__(self,Roll_Number,Year,Semester,Email):
        self._Roll_Number = Roll_Number
        self._Year = Year
        self._Semester = Semester
        self._Email = Email
        self.next = None
        
    def Display_Nodes(self):
        print("The node in stack is: ", self._Roll_Number,self._Year,self._Semester,self._Email)
    
    def Get_Roll_Number(self):
        return self._Roll_Number
    
class Stack_Students:
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
            print("Your stack of students is empty")
            return
        else:
            temp = self.head
            self.head = self.head.next
            temp = None
            self.size = self.size - 1

    def Size(self):
        print("The size of your stack_Students is: ", self.size)
    
    def Find_Roll_Number(self, Roll_Number):
        Temp = self.head
        while Temp is not None:
            if Temp.Get_Roll_Number() == Roll_Number:
                print('Roll_Number is present in the Stack')
                break
            if Temp.Get_Roll_Number() != Roll_Number:
                if Temp.next == None:
                    print('Roll_Number is not present in the Stack')

            Temp = Temp.next
        
    def Print_Stack(self):
        if self.head == None:
            print("Your stack is empty")
        Temp = self.head
        while Temp != None:
            Temp.Display_Nodes()
            Temp = Temp.next
            
    def Display(self):
        Do = input("Please Press S to start the program: ")
        OBJ = Stack_Students()
        while Do != "f":
            choice = input("pleased enter your choice from a,b,c,d,e,f: ") 
            if choice == "a":
                loop = input("enter how many time you want to insert node: ")
                for i in range(int(loop)):
                    Roll_Number = int(input("please enter the Roll_Number of Student: "))
                    Year = int(input("please enter the Year of Studennt: "))
                    Semester = input("please enter the Semester of Studennt: ")
                    Email = input("please enter the Email of Studennt: ")
                    OBJ.Push(Node(Roll_Number,Year,Semester,Email))
                OBJ.Print_Stack()
            elif choice == "b":
                OBJ.POP()
                OBJ.Print_Stack()
            elif choice == "c":
                OBJ.Size()
            elif choice == "d":
                Roll_Number = int(input("Enter Roll Number to search: "))
                OBJ.Find_Roll_Number(Roll_Number)
            elif choice == "e":
                OBJ.Print_Stack()
            elif choice == "f":
                print("Thank you for chosing my menu Bye Bye")
                break
OBJ = Stack_Students()
OBJ.Display()
