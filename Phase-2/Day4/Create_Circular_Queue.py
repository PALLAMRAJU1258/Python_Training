class CircularQueue():
    def __init__(self,size):
        self.size = size
        self.queue = [None for i in range(size)]
        self.front = self.rear = -1

    def enqueue(self,data):
        if ((self.rear+1)%self.size == self.front):
            print("Queue is Full\n")
        elif self.front == -1:
            self.front = 0
            self.rear = 0
            self.queue[self.rear] = data
        else:
            self.rear = (self.rear + 1)% self.size
            self.queue[self.rear] = data

    def dequeue(self):
        if self.front == -1:
            print("Queue is empty\n")
        elif self.rear == self.front :
            temp == self.queue[self.front]
            self.front = -1
            self.rear = -1
            return temp
        else:
            temp = self.queue[self.front]
            self.front = (self.front+1)%self.size
            return temp

    def is_rear_greater_than_front(self):
        return self.rear > self.front and ((self.rear + 1) % self.size) == self.front

    def display(self):
        if self.front == -1:
            print("Queue is empty")
        elif self.rear >= self.front:
            print("Elements in the circular queue are:",end=" ")
            for i in range(self.front,self.rear+1):
                print(self.queue[i],end=" ")
            print()
        else:
            print("Elements in Circular Queue are:",end=" ")
            for i in range(self.front,self.size):
                print(self.queue[i],end=" ")
            for i in range(0,self.rear+1):
                print(self.queue[i],end=" ")
            print()

        if (self.rear+1) % self.size == self.front :
            print("Queue is Full")


obj = CircularQueue(5)
obj.enqueue(14)
print(obj.is_rear_greater_than_front())
obj.enqueue(1)
print(obj.is_rear_greater_than_front())
obj.enqueue(10)
print(obj.is_rear_greater_than_front())
obj.enqueue(35)
print(obj.is_rear_greater_than_front())
obj.enqueue(32)
print(obj.is_rear_greater_than_front())
obj.display()
print("Removed element is:",obj.dequeue())
print("Removed element is:",obj.dequeue())
obj.display()
obj.enqueue(23)
obj.enqueue(18)
obj.display()
