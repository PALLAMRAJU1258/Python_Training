"""write a program using nested if to check the number's range in the 10th position 
if number is equal to 21 then range must be 20 to 30 
if the number is 7 the range must be zero to 10"""

#using nested if
a=int(input("Enter the value between 0 to 30:"))
if num >= 0 and num < 10:
    print("range is 0-10")
elif num >=10 and num < 20:
    print("range is 10-20")
elif num >=20 and num < 30:
    print("range is 20-30")
else:
    print("range exceeded")

"""
#without using nested if
a=int(input())
te=a%10
s=(a-te)+10
print("{0} between {1} and{2}".format(a,a-te,s))
"""
