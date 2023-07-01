class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class SingleLinkedList:
    def __init__(self):
        self.head = None
        
    def display(self):
        if self.head is None :
            print("linked list is empty")
        else:
            temp = self.head
            print("Head ==>",end = " ")
            while(temp):
                print(temp.data,"==>",end = " ")
                temp = temp.next
            print("Null",end = "\n\n")
            
    def delete_At_Beginning(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        
        
obj = SingleLinkedList()
n1 = Node(10)
obj.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
obj.display()
obj.delete_At_Beginning()
obj.display()
