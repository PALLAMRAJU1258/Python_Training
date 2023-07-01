"""
You  are given an integer,N.Your task is to print an alphabet rangoli of size N.
(Rangoli is a form of Indian folk art based on creation of patterns.)
Different sizes of alphabet rangoli are shown below:
Size 3
----c----
--c-b-c--
c-b-a-b-c
--c-b-c--
----c----

Size 5
--------e--------
------e-d-e------
----e-d-c-d-e----
--e-d-c-b-c-d-e--
e-d-c-b-a-b-c-d-e
--e-d-c-b-c-d-e--
----e-d-c-d-e----
------e-d-e------
--------e--------
"""
import string
def print_rangoli(size):
    design=string.ascii_lowercase
    li=[]
    for i in range(n):
        s="-".join(design[i:n])
        li.append((s[::-1]+s[1:]).center(4*n-3,"-"))
    print('\n'.join(li[:0:-1]+li))
n=int(input())
print_rangoli(n)
