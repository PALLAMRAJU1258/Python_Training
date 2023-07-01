class Node:
    def __init__(self,data):
        self.data = data
        self.prev = None
        self.next = None
        
class DLL:
    def __init__(self):
        self.head = None
        
    def delete_Particular_Node(self,position):
        if position == 1 :
            temp = self.head
            temp.prev = None
            self.head = temp.next
            temp.next = None
            self.head.prev = None
        else:
            left_node = self.head
            right_node = left_node.next
            for i in range(1,position-1):
                left_node = left_node.next
                right_node = right_node.next
            temp = left_node.next
            left_node.next = temp.next
            right_node.prev = temp.prev
            temp.next = None
            temp.prev = None
        
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
            
    def Length(self):
        self.count=0
        temp = self.head
        while temp :
            self.count += 1
            temp = temp.next
        return self.count


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
obj.delete_Particular_Node(1)
obj.display()
obj.delete_Particular_Node(int(input(f"Enter the position of node to delete (The linked list conisit of {obj.Length()} elements):")))
obj.display()
        
