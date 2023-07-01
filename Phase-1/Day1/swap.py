#Write a program to swap two numbers
a=int(input("Enter the value:"))
b=int(input("Enter the value:"))
#swapping the numbers using assignment operator
print("before swapping:",a, b)
b,a=a,b
print("swapping the numbers using assignment operator:",a, b)

#swapping the numbers by applying addition and subtraction
a=a+b
b=a-b
a=a-b
print("swapping the numbers by applying addition and subtraction:",a,b)

#swapping the numbers by multiplication and division

a=a*b 
b=a/b 
a=a/b 
print("swapping the numbers by multiplication and division",int(a),int(b))
