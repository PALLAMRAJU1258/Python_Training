stack_1 = []
stack_2 = []
i=0
j=0
def push(data,i,j):
    if data % 2 == 0 and i <= 5:
            stack_1.append(data)
            
    elif data % 2 != 0 and j <= 5 :
            stack_2.append(data)
            

def pop_element():
    ch = input("Enter the which type of value to remove even or odd:") 
    if  ch == "even":
        stack_1.pop()
    elif ch == "odd":
        stack_2.pop()


while True :
    
    print("Select the Operation\n1.push\n2.pop\n3.display\n4.quit")
    choice = int(input("Enter the choice:"))
    if choice == 1 :
        data = int(input("Enter the value:"))
        if data % 2 == 0 :
                   i+=1
        else :
            j += 1
        if i <= 5 or j <= 5 :
            push(data,i,j)
    elif choice == 2 :
        pop_element()
    elif choice == 3 :
        print("Even stack:",stack_1)
        print("Odd stack:",stack_2)
    elif choice == 4:
        break
    else:
        print("Enter correct choice.")
