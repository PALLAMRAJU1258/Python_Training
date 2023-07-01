"""
Write a program to calculate sum of series shown below:
1/2+2/3+3/4+.......................
"""
n=int(input("Enter the value:"))
sum=0.0
for i in range(1,n+1):
    sum+=(i/i+1)
print("sum of n/n+1 series is:",sum)
