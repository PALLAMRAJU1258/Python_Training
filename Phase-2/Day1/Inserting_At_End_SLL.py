"""
Insert at end-
Step1:Create new node which you want to insert
Step2:make the new node point to previous last node
Step3:make your new node next pointer as null
"""
#Write a program to insert a element at end of the SLL(Single Linked List)
class Node:
    def __init__(self,data):
        self.data = data
        self.next = None
class SingleLinkedList:
    def __init__(self):
        self.head = None
    def insert_AtEnd(self,data):
        ne=Node(data)
        temp=self.head
        while temp.next :
            temp=temp.next
        temp.next=ne
        
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
obj.insert_AtEnd(100)
print("After inserting 100 at beginning")
obj.display()
obj.insert_AtEnd(input())
print("After inserting another element at beginning")
obj.display()

