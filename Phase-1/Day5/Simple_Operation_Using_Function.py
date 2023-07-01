"""
Write a program to do a operation(+,-,*,/,//,%) given by user using functions
"""
def operation(num1,num2,op):
    if op =="+" :
        print("Addition of {} and {} is : {}".format(num1,num2,num1+num2))
    elif op == "-" :
        print("Subtract of {} with {} is : {}".format(num1,num2,num1-num2))
    elif op == "*" :
        print("Multiplication of {} and {} is : {}".format(num1,num2,num1*num2))
    elif op =="/" :
        print("Division of {} and {} is :{}".format(num1,num2,num1/num2))
    elif op == "//" :
        print("Floor Division of {} and {} is : {}".format(num1,num2,num1//num2))
    elif op == "%" :
        print("modular Division of {} and {} is :{}".formart(num1,num2,num1%num2))
    else:
        print("Please Enter the given operators.")
n1=int(input("Enter the value:"))
n2=int(input("Enter the value:"))
op=input("Choose +,-,*,/,//,%:")
operation(n1,n2,op)





