class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
class DLL:
    def __init__(self):
        self.head = None
        
    def insert_Between_Nodes(self,data,position):
        nd = Node(data)
        temp = self.head
        for i in range(position-1):
            temp = temp.next
        nd.prev = temp.next.prev
        nd.next = temp.next
        temp.next = nd
        temp.next = nd

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

    def Length(self,count):
        temp = self.head
        while temp :
            count+=1
            temp = temp.next
        return count

            
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
obj.insert_Between_Nodes(100,2)
obj.display()
print(f"The Linked List consist of {obj.Length(0)} elements")
obj.insert_Between_Nodes(input("Enter the element to insert:"),int(input("Enter the position where to insert:")))
obj.display()

        
