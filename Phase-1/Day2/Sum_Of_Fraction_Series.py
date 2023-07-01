'''Write a program to calculate sum of 1/n fraction series where n is natural
number'''
n=int(input("Enter a natural value:"))
sum=0
for i in range(1,n+1):
    sum+=(1/i)
print("sum of 1/n fraction series where n is natural number:",sum)
