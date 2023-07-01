class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
        
class SingleLinkedList:
    def __init__(self):
        self.head = None
        
    def insert_Between_Nodes(self,data,position):
        nd = Node(data)
        temp = self.head
        for i in range(position-1):
            temp = temp.next
        nd.next = temp.next
        temp.next=nd
        
    def Length(self,count):
        temp=self.head
        while temp :
            count+=1
            temp = temp.next
        return count
          
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

            
obj = SingleLinkedList()
n1 = Node(10)
obj.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
obj.display()
obj.insert_Between_Nodes(100,2)
obj.display()
print(f"The Linked List consist of {obj.Length(0)} elements")
obj.insert_Between_Nodes(input("Enter the element to insert:"),int(input("Enter the position where to insert:")))
obj.display()
