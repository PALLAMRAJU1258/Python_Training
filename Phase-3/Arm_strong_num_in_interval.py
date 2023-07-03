def arm_strong(sum,n):
    r=n%10
    sum+=r**3
    n//=10
    if n == 0:
        return sum
    else:
        return arm_strong(sum,n)

start = int(input())
end = int(input())
list =[]
for i in range(start,end+1):
    if i == arm_strong(0,i):
        list.append(i)
    else:
        pass
print(list)
