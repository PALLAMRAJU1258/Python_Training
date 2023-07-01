"""
Write a program to demonstrate the use of variable lenght in function and
calculating the sum of elements of list using function
"""
def sum_of_list(*var):
    sum=0
    print(type(var))
    print(var)
    for i in var:
        sum+=i
    return sum
n1=int(input())
n2=float(input())
n3=int(input())
print(sum_of_list(n1,n2,n3))

