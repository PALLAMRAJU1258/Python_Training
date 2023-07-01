#Write a program to calculate sum of elements in lists using functions
def sum_of_list(li_1,sum=0):
    for i in li_1:
        sum+=i
    return sum
li_1=list(map(int,input("Enter  numeric value only:").split(",")))
print("Sum of elements of list:",sum_of_list(li_1))

    
"""
Another method
def sum_of_list(li):
    return sum(li)
li=list(map(int,input("Enter numeric value only:").split(",")))
print("Sum of elements of list:",sum_of_list(li))
"""
