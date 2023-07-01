"""
Linked List:
Linked List is a sequence of links which contains items.
Each link contains a connection to another link.

Type of Linked List:
1)Single Linked List
2)Double Linked List
3)Circular Linked List

Insert Operation of SLL:
1)Insert element at beginning
2)Insert element at end
3)Insert element between nodes
"""
#Write a program to create a Single Linked List
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SLL:
    def __init__(self):
        self.head = None
    def display(self):
        if self.head is None :
            print("Linked list is empty")
        else:
            temp = self.head
            print("Head ==>",end = " ")
            while(temp):
                print(temp.data,"==>",end = " ")
                temp = temp.next
            print("Null")
        

obj = SLL()
n1 = Node(100)
obj.head = n1
n2 = Node(200)
n1.next = n2
n3 = Node(300)
n2.next = n3
obj.display()
