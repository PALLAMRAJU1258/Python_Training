queue = []
def enqueue():
    element = input("Enter the element:")
    queue.append(element)
    print(element,"is added in queue")

def dequeue():
    if not queue:
        print("Queue is empty")
    else:
        e = queue.pop(0)
        print("removed element:",e)

def display():
    print(queue)

while True :
    print("Select the opertaion\n1.add\n2.remove\n3.display\n4.exit")
    choice = int(input())
    if choice == 1:
        enqueue()
    elif choice == 2:
        dequeue()
    elif choice == 3:
        display()
    else:
        print("Enter Correct Choice")
