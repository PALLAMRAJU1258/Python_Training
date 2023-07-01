"""Write a program to calculate the total of N natural number
find it's average n=10"""
n=int(input("Enter the number:"))
sum=0
for i in range(1,n+1):
    sum+=i
avg=sum/n
print("sum of {0} natural numbers is :{1}".format(n,sum))
print("average of {0} natural numbers is:{1}".format(n,avg))
    
