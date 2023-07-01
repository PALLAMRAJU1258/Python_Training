"""
Write a program to print a series of number shown below when an number n is
given

n=5
5 16 8 4 2 1

n=6
6 3 10 5 16 8 4 2 1

n=7
7 22 11 34 17 52 26 13 40 20 10 5 16 8 4 2 1
"""
def series(n):
    li=[]
    li.append(n)
    while n != 1:
        if n % 2 == 0:
            n=n//2
            li.append(n)
        else:
            n=(n*3)+1
            li.append(n)
    return li
n=int(input())
list_series=series(n)
for i in list_series:
    print(i,end=" ")
