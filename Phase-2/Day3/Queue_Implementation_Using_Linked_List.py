class Node :
    def __init__(self,data):
        self.data = data
        self.next = None

class Queue :
    def __init__(self):
        self.head = None
        self.last = None

    def enqueue(self,data):
        if self.last is None:
            self.head = Node(data)
            self.last = self.head
        else:
            self.last.next = Node(data)
            self.last = self.last.next

    def dequeue(self):
        if self.head is None :
            return None
        else:
            temp = self.head
            To_return = temp.data
            self.head = temp.next
            temp.next = None
            return To_return

    def display(self):
        temp = self. head
        print("head",end=" -->")
        while temp :
            print(temp.data,end=" --> ")
            temp = temp.next
        if temp != self.last :
            print("last")

a_queue = Queue()
while True :
    print("\nenqueue <value>")
    print("dequeue")
    print("display")
    print("quit")
    do = input("What would you like to do?").split(" ")
    operation = do[0].strip().lower()
    if operation == "enqueue": 
       a_queue.enqueue(int(do[1]))
    elif operation == "dequeue":
        dequeued = a_queue.dequeue()
        if dequeued is None :
            print("Queue is empty")
        else:
            print("Dequeued element:",int(dequeued))
    elif operation == "display" :
        a_queue.display()

    elif operation == "quit" :
        break
    else:
        print("Enter the correct operation.")
        
