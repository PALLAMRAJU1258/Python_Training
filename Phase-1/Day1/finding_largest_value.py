#Write a program to find the largest number from given numbers
a=int(input("Enter the first value:"))
b=int(input("Enter the second value:"))
c=int(input("Enter the third value:"))
if a>b:
    if a>c :
        print("a is greater")
    else:
        print("c is greater")
elif b>c :
    print("b is greater")
else:
    print("equal")
