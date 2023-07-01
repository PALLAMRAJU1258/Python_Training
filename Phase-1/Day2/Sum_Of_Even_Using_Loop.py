#Write a program to calculate sum of even numbers from given n numbers
n=int(input("Enter the number:"))
i,sum=1,0
while(i<=n):
    if(i%2==0):
        sum=sum+i
    i=i+1
print(sum)
