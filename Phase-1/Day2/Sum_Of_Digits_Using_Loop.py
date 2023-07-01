#Write a program to add all the digits in a number
n=int(input("Enter the value:"))
digit=sum=0
while(n!=0):
    digit=n%10
    sum+=digit
    n=n//10
print("Sum of individual digits in given number is:",sum)
