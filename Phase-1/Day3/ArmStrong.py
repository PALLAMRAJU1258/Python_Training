#Write a program to check whether the given number is armstrong or not
num=int(input("Enter the value:"))
temp=num
sum=0
while temp!=0:
    r=temp%10
    sum=sum+(r**3)
    temp=temp//10
if(sum==num):
    print("Given number {} is armstrong".format(num))
else:
    print("Given number",num," is not armstrong")
    
    
