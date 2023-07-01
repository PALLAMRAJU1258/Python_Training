#Write a program to find the given term in given below series
#0,0,7,6,14,12,21,.....n

a=7
b=6
i=j=temp=1
list_=[]
n=int(input("Enter n:"))
while(temp<=n):
    if temp%2!=0:
        list_.append(a*(i-1))
        i+=1
    else:
        list_.append(b*(j-1))
        j+=1
    temp+=1
print(list_)
print("the {} term is:{}".format(n,list_[n-1]))
"""#Another method
list1=[]
list2=[]
a,b=7,6
i=j=1
temp=0
n=int(input("Enter n:"))
while(temp<=n):
    if temp%2!=0:
        list1.append(a*(i-1))
        i+=1
    else:
        list2.append(b*(j-1))
        j+=1
    temp+=1
i=j=0
while i<(len(list2)):
    a=list2[i]
    list1.insert(j+1,a)
    j+=2
    i+=1
print(list1)
print("the {} term is:{}".format(n,list1[n-1]))"""

