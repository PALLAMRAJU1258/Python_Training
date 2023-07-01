#Write a program to convert decimal to binary
dn=int(input("enter the number:"))
bn=0
i=0
while dn!=0:
    r=dn%2
    bn=bn+r*(10**i)
    dn=dn//2
    i=i+1
print(bn)
