"""
A washing machine works on the principle of fuzzy system,the weight of clothes
put inside it for washing is uncertain but based on weight measured by sensors,
it decides time and water level which can be changed by menus given on the
machine control area.

for low level water, the time estimate is 25 minutes, where approximately weight
is between 2000 grams or any non zero positive number below that

for medium level water, the time estimate is 35 minutes, where approximately
weight is between 2001 grams and 4000 grams

for high level water, the time estimate is 45 minutes, where approximately
weight is above 4000 grams

Assume the capacity of machine is maximum 7000 grams

Where approximately weight is zero, time estimate is 0 minutes.

Write a function which takes a numeric weight in range [0,7000] as input and
produces estimated time as output is: "OVERLOADED",and for all other inputs,
the output statement is "INVALID INPUT"
Input should be in the form of integer value-
Output must have the following format-
Time Estimated:<Integer> Minutes
"""
def calculate_Time(n):
    if (n==0):
        print("Time Estimated:0 Minutes")
    elif (n>0) and (n<=2000):
        print("Time Estimated:25 Minutes")
    elif (n>2000) and (n<=4000):
        print("Time Estimated:35 Minutes")
    elif (n>4000) and (n<=7000):
        print("Time Estimated:45 Minutes")
    else:
        print("INVALID INPUT")
machine_weight=int(input())
calculate_Time(n)
        
