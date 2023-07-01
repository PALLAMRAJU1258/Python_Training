"""
Insert at begining-
Step1:Create new node which you want to insert
Step2:make the new node point to current head node
Step3:make your new node as head node
"""
#Write a program to insert a element at beginning of SLL(Single Linked List)
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.head = None
    def insert_Atbeginning(self,data):
        nb = Node(data)
        nb.next = self.head
        self.head = nb
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
print("Before inserting 100 at beginning")
obj.display()
obj.insert_Atbeginning(100)
print("After inserting 100 at beginning")
obj.display()
obj.insert_Atbeginning(input())
print("After inserting another element at beginning")
obj.display()

