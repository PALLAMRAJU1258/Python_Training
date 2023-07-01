class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class stack:
    def __init__(self):
        self.head = None

    def push(self,data):
        if self.head is None :
            self.head = Node(data)
        else:
            nd = Node(data)
            nd.next = self.head
            self.head = nd

    def pop_element(self):
        if self.head is None:
            print("Stack is underflow")
        else:
            print("removed element is:",self.head.data)
            top = self.head
            self.head = top.next
            top.next = None

    def display(self):
        if self.head is None:
            print("Stack is underflow")
        else:
            top = self.head
            while top:
                print(top.data,end=" ")
                top = top.next
                if top is not None:
                    print("-->",end=" ")
            print("")


obj = stack()
while True:
    print("Select the operation\n1.push\n2.pop\n3.display\n4.exit")
    choice = int(input("Enter the choice:"))
    if choice == 1:
        obj.push(int(input("Enter the element to insert in stack:")))
    elif choice == 2:
        obj.pop_element()
    elif choice == 3:
        obj.display()
    elif choice == 4:
        break
    else:
        print("Enter correct choice.")
