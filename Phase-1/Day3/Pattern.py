"""Write a program to print a pattern as shown in below
A
AB
ABC
ABCD
ABCDE
.........................
.........................
"""
n=int(input("Enter the number of rows should print:"))
for i in range(1,n+1):
    ch='A'
    print()
    for j in range(1,i+1):
        print(ch,end=" ")
        ch=chr(ord(ch)+1)
        
