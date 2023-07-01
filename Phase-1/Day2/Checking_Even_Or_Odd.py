#Write a program to print even numbers and odd numbers from given n numbers
n=int(input("Enter the number:"))
i=1
while(i<=n):
    if(i%2==0):
        print(i,"is a even number")
    else:
        print(i,"is  a odd number")
    i=i+1
