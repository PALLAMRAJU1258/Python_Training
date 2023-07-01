class Node:
    def __init__(self,data):
        self.data = data
        self.next = None

class CLL:
    def __init__(self):
        self.head = None

    def display(self):
        temp = self.head
        if temp is None :
            print("The linked list is empty")
        else:
            print("Head",end=" --> ")
            i=1
            while temp :
                print("Node {}:{}".format(i,temp.data),end=" ")
                temp = temp.next
                if temp == self.head :
                    i=1
                    print("--> Node {}:{}".format(i,temp.data))
                    break
                else:
                    i +=1
                    print("-->",end=" ")
        
                
obj = CLL()
n1 = Node(10)
obj.head = n1
n2 = Node(20)
n1.next = n2
n3 = Node(30)
n2.next = n3
n4 = Node(40)
n3.next = n4
n4.next = n1
obj.display()
