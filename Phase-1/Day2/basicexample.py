'''Write a program to calculate the sum of even and odd digits from given number
and find the difference of odd sum and even sum
'''
n=int(input("Enter the number:"))
sum_1=0
sum_2=0
while(n!=0):
    r=n%10
    if(r%2==0):
        sum_1+=r
    else:
        sum_2+=r
    n=n//10
print("sum of even digits from given number is:",sum_1)
print("sum of odd digits from given number is:",sum_2)
print("diference of odd sum and even sum is:",sum_2-sum_1)
