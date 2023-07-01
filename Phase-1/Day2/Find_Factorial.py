#Write a program to calculate the factorial of given number
num=int(input("Enter the number:"))
fact=1
i=1
if(num==0) or (num==1):
    print("factorial of {0} is:{1}".format(num,fact))
else:
    while(i<=num):
        fact=fact*i
        i+=1
    print("factorial of {0} is:{1}".format(num,fact))
    
