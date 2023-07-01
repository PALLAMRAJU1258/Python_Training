class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
class DLL:
    def __init__(self):
        self.head = None
        
    def delete_At_Beginning(self):
        temp = self.head
        self.head = temp.next
        temp.next = None
        temp.prev = None
        self.head.prev = None
        
    def display(self):
        temp = self.head
        if temp is None :
            print("The linked list is empty")
        else:
            print("Head",end=" --> ")
            while temp :
                print(temp.data,end=" ")
                temp = temp.next
                if temp is not None :
                    print("<-->",end=" ")
            print("--> NULL",end="\n\n")


obj = DLL()
n1 = Node(10)
obj.head = n1
n2 = Node(20)
n1.next = n2
n2.prev = n1
n3 = Node(30)
n2.next = n3
n3.prev = n2
n4 = Node(40)
n3.next = n4
n4.prev = n3
obj.display()
obj.delete_At_Beginning()
obj.display()


        
